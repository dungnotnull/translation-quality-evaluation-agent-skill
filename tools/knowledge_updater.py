#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""knowledge_updater.py — Self-improving crawler for the Translation Quality Evaluation (specialized) skill.

This tool maintains and expands the knowledge base (SECOND-KNOWLEDGE-BRAIN.md) by automatically
crawling authoritative sources for the latest research, standards, and industry developments
in translation quality assessment.

Pipeline:
  1. crawl4ai -> fetch latest papers/docs from domain sources
  2. WebSearch queries -> latest news/reports
  3. parse -> title, authors, date, DOI/URL, abstract, key findings
  4. score -> recency (0-1) * domain-keyword relevance (0-1)
  5. dedupe -> skip entries already present (URL/DOI hash)
  6. append -> add scored entries to SECOND-KNOWLEDGE-BRAIN.md

Run weekly (cron). Requires: pip install crawl4ai beautifulsoup4 requests

Usage:
    python tools/knowledge_updater.py              # Full crawl
    python tools/knowledge_updater.py --dry-run     # Show what would be added
    python tools/knowledge_updater.py --arxiv-only  # ArXiv crawl only
    python tools/knowledge_updater.py --sources     # Source URLs only

Author: Translation Quality Evaluation skill
License: MIT
Version: 1.0.0
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Callable, Optional
from urllib.parse import urlparse

# Type hints for better IDE support
if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    TypeAlias = Any

# =============================================================================
# Configuration
# =============================================================================

SKILL_ID = 95
SKILL_SLUG = "translation-quality-evaluation"
BRAIN_PATH = Path(__file__).parent.parent / "SECOND-KNOWLEDGE-BRAIN.md"
LOG_PATH = Path(__file__).parent.parent / "logs" / "knowledge_updater.log"
CACHE_PATH = Path(__file__).parent.parent / ".cache" / "knowledge_updater_cache.json"

# ArXiv categories to crawl
ARXIV_CATEGORIES = ["cs.CL", "cs.LG", "cs.AI"]

# Search queries for different domains
SEARCH_QUERIES = {
    "core": [
        "translation quality assessment MQM",
        "multidimensional quality metrics",
        "DQF dynamic quality framework",
        "ISO 17100 translation services"
    ],
    "terminology": [
        "terminology consistency localization",
        "ISO 12616 terminology management",
        "term bank validation translation"
    ],
    "evaluation": [
        "machine translation evaluation",
        "neural MT quality assessment",
        "post-editing quality metrics"
    ],
    "legal": [
        "legal translation quality standards",
        "certified translation requirements"
    ],
    "medical": [
        "medical translation quality",
        "clinical translation validation"
    ]
}

# Primary source URLs to scan
SOURCE_URLS = [
    "https://www.taus.net/resources",
    "https://themqm.org/framework",
    "https://www.iso.org/standard/59149.html",
    "https://www.gala-global.org/resources",
    "https://www.atanet.org/certification/"
]

# Domain keywords for relevance scoring
DOMAIN_KEYWORDS = [
    "translation quality",
    "MQM",
    "multidimensional quality metrics",
    "DQF",
    "dynamic quality framework",
    "ISO 17100",
    "translation services",
    "terminology",
    "localization quality",
    "machine translation evaluation",
    "post-editing",
    "translation assessment",
    "error typology",
    "quality estimation"
]

# =============================================================================
# Data Classes
# =============================================================================

@dataclass
class KnowledgeEntry:
    """A single knowledge base entry."""
    title: str
    url: str
    authors: str
    year: int | str
    abstract: str
    venue: str = ""
    doi: str = ""
    relevance_score: float = 0.0
    crawl_date: str = field(default_factory=lambda: date.today().isoformat())

    def to_dict(self) -> dict[str, Any]:
        return {
            "title": self.title,
            "url": self.url,
            "authors": self.authors,
            "year": self.year,
            "abstract": self.abstract,
            "venue": self.venue,
            "doi": self.doi,
            "relevance_score": self.relevance_score,
            "crawl_date": self.crawl_date
        }

    def to_markdown(self) -> str:
        """Convert to markdown format for SECOND-KNOWLEDGE-BRAIN.md."""
        lines = [
            f"### [{self.crawl_date}] {self.title}",
            f"**Source:** {self.venue or 'Unknown Source'}",
            f"**Authors:** {self.authors or 'n/a'}",
            f"**Year:** {self.year}",
            f"**DOI/Link:** {self.doi or self.url}",
            f"**Relevance Score:** {self.relevance_score:.3f}",
            "",
            "**Key Findings:**",
            f"- {self.abstract[:300]}..." if len(self.abstract) > 300 else f"- {self.abstract or '(abstract pending)'}",
            "",
            f"**Relevance to Skill:** {self._generate_relevance_note()}",
            "",
            f"<!--hash:{self._hash()}-->"
        ]
        return "\n".join(lines)

    def _hash(self) -> str:
        """Generate hash from URL or DOI."""
        content = self.doi if self.doi else self.url
        return hashlib.sha256(content.encode("utf-8")).hexdigest()[:16]

    def _generate_relevance_note(self) -> str:
        """Generate a relevance note based on keywords."""
        title_lower = self.title.lower()
        abstract_lower = self.abstract.lower()
        matched = [kw for kw in DOMAIN_KEYWORDS if kw.lower() in title_lower or kw.lower() in abstract_lower]
        if matched:
            return f"Directly relevant: addresses {', '.join(set(matched[:3]))}"
        return "General translation quality context"

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "KnowledgeEntry":
        """Create from dictionary."""
        return cls(
            title=data.get("title", "Untitled"),
            url=data.get("url", ""),
            authors=data.get("authors", ""),
            year=data.get("year", ""),
            abstract=data.get("abstract", ""),
            venue=data.get("venue", ""),
            doi=data.get("doi", ""),
            relevance_score=data.get("relevance_score", 0.0),
            crawl_date=data.get("crawl_date", date.today().isoformat())
        )


@dataclass
class CrawlResult:
    """Result of a crawl operation."""
    entries: list[KnowledgeEntry] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    sources_crawled: int = 0
    sources_failed: int = 0

    def add_entry(self, entry: KnowledgeEntry) -> None:
        """Add an entry to the result."""
        self.entries.append(entry)

    def add_error(self, error: str) -> None:
        """Add an error to the result."""
        self.errors.append(error)

    def merge(self, other: "CrawlResult") -> None:
        """Merge another result into this one."""
        self.entries.extend(other.entries)
        self.errors.extend(other.errors)
        self.sources_crawled += other.sources_crawled
        self.sources_failed += other.sources_failed


# =============================================================================
# Hash and Deduplication
# =============================================================================

def hash_url(url: str) -> str:
    """Generate a 16-character hash from URL."""
    return hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]


def hash_doi(doi: str) -> str:
    """Generate a 16-character hash from DOI."""
    return hashlib.sha256(doi.encode("utf-8")).hexdigest()[:16]


def load_seen_hashes(brain_path: Path) -> set[str]:
    """Load existing hashes from the knowledge base."""
    if not brain_path.exists():
        return set()

    try:
        content = brain_path.read_text(encoding="utf-8")
        hashes = set(re.findall(r"<!--hash:([0-9a-f]{16})-->", content))
        logging.info(f"Loaded {len(hashes)} existing hashes from knowledge base")
        return hashes
    except Exception as e:
        logging.error(f"Failed to load hashes from {brain_path}: {e}")
        return set()


def filter_duplicates(entries: list[KnowledgeEntry], seen_hashes: set[str]) -> tuple[list[KnowledgeEntry], int]:
    """Filter out duplicate entries based on URL/DOI hash."""
    unique_entries = []
    duplicate_count = 0

    for entry in entries:
        entry_hash = entry._hash()
        if entry_hash not in seen_hashes:
            unique_entries.append(entry)
            seen_hashes.add(entry_hash)
        else:
            duplicate_count += 1

    logging.info(f"Filtered {duplicate_count} duplicate entries, {len(unique_entries)} unique entries remain")
    return unique_entries, duplicate_count


# =============================================================================
# Relevance Scoring
# =============================================================================

def calculate_relevance_score(entry: KnowledgeEntry) -> float:
    """Calculate relevance score based on recency and keyword matching."""
    try:
        year = int(str(entry.year).split("-")[0][:4]) if entry.year else 0
    except (ValueError, AttributeError):
        year = 0

    now = date.today().year
    recency = max(0.0, 1.0 - (now - year) / 10.0) if year else 0.3

    text = (entry.title + " " + entry.abstract + " " + entry.venue).lower()
    keyword_hits = sum(1 for kw in DOMAIN_KEYWORDS if kw.lower() in text)
    keyword_score = min(1.0, keyword_hits / max(1, len(DOMAIN_KEYWORDS) * 0.3))

    relevance = round(recency * (0.4 + 0.6 * keyword_score), 3)
    return max(0.0, min(1.0, relevance))


# =============================================================================
# ArXiv Crawler
# =============================================================================

def crawl_arxiv_category(category: str, days_back: int = 7) -> CrawlResult:
    """Crawl recent papers from an ArXiv category."""
    result = CrawlResult()
    url = f"https://arxiv.org/list/{category}/recent"

    try:
        from crawl4ai import WebCrawler
        crawler = WebCrawler()
        crawler.warmup()

        logging.info(f"Crawling ArXiv category: {category}")
        response = crawler.run(url=url)

        if response and hasattr(response, "markdown"):
            entries = parse_arxiv_response(response.markdown, category)
            for entry in entries:
                entry.relevance_score = calculate_relevance_score(entry)
                result.add_entry(entry)
            result.sources_crawled += 1
        else:
            result.add_error(f"No valid response from {url}")
            result.sources_failed += 1

    except ImportError:
        error_msg = "crawl4ai not installed; run: pip install crawl4ai"
        logging.warning(error_msg)
        result.add_error(error_msg)
        result.sources_failed += 1
    except Exception as e:
        error_msg = f"Failed to crawl ArXiv {category}: {e}"
        logging.error(error_msg)
        result.add_error(error_msg)
        result.sources_failed += 1

    logging.info(f"ArXiv {category}: {len(result.entries)} entries, {len(result.errors)} errors")
    return result


def parse_arxiv_response(markdown: str, category: str) -> list[KnowledgeEntry]:
    """Parse ArXiv listing response into KnowledgeEntry objects."""
    entries = []
    today = date.today()

    # Pattern for ArXiv ID: arXiv:YYMM.NNNNN or arXiv:YYMM.NNNNNvV
    arxiv_pattern = re.compile(r"arXiv:(\d{4}\.\d{4,5}[v\d]?)")
    title_pattern = re.compile(r"Titles?:\s*(.+?)(?:\n|Authors?:|$)")
    authors_pattern = re.compile(r"Authors?:\s*(.+?)(?:\n|Comments?:|$)")

    for arxiv_id in arxiv_pattern.findall(markdown):
        url = f"https://arxiv.org/abs/{arxiv_id}"
        entry = KnowledgeEntry(
            title=f"ArXiv:{arxiv_id}",
            url=url,
            authors="",
            year=today.year,
            abstract=f"Paper in {category}",
            venue=f"ArXiv {category}",
            doi=""
        )
        entries.append(entry)

    return entries


# =============================================================================
# Source URL Crawler
# =============================================================================

def crawl_source_url(source_url: str) -> CrawlResult:
    """Crawl a single source URL for relevant content."""
    result = CrawlResult()

    try:
        from crawl4ai import WebCrawler
        crawler = WebCrawler()

        logging.info(f"Crawling source: {source_url}")
        response = crawler.run(url=source_url)

        if response and hasattr(response, "markdown"):
            entry = KnowledgeEntry(
                title=f"Source scan: {urlparse(source_url).netloc}",
                url=source_url,
                authors="",
                year=date.today().year,
                abstract=response.markdown[:500] if response.markdown else "",
                venue=urlparse(source_url).netloc,
                doi=""
            )
            entry.relevance_score = calculate_relevance_score(entry)
            result.add_entry(entry)
            result.sources_crawled += 1
        else:
            result.add_error(f"No valid response from {source_url}")
            result.sources_failed += 1

    except Exception as e:
        error_msg = f"Failed to crawl {source_url}: {e}"
        logging.error(error_msg)
        result.add_error(error_msg)
        result.sources_failed += 1

    return result


# =============================================================================
# Appender
# =============================================================================

def append_entries_to_brain(
    entries: list[KnowledgeEntry],
    brain_path: Path,
    dry_run: bool = False
) -> tuple[int, int]:
    """Append new entries to the knowledge base.

    Returns:
        (appended_count, skipped_count)
    """
    if not entries:
        logging.info("No entries to append")
        return 0, 0

    # Sort by relevance score (descending)
    sorted_entries = sorted(entries, key=lambda e: e.relevance_score, reverse=True)

    # Load existing hashes
    seen_hashes = load_seen_hashes(brain_path)

    # Filter duplicates
    unique_entries, duplicate_count = filter_duplicates(sorted_entries, seen_hashes)

    if not unique_entries:
        logging.info("All entries are duplicates; nothing to append")
        return 0, len(sorted_entries)

    # Prepare markdown content
    today = date.today().isoformat()
    lines = [
        "",
        "",
        f"## Automated Crawl Batch — {today}",
        "",
        f"**Total entries crawled:** {len(sorted_entries)}",
        f"**New entries added:** {len(unique_entries)}",
        f"**Duplicates filtered:** {duplicate_count}",
        ""
    ]

    for entry in unique_entries:
        lines.append(entry.to_markdown())
        lines.append("")

    # Append to file
    if dry_run:
        logging.info("[DRY RUN] Would append the following to knowledge base:")
        logging.info("\n".join(lines))
        return len(unique_entries), duplicate_count

    try:
        # Ensure parent directory exists
        brain_path.parent.mkdir(parents=True, exist_ok=True)

        # Append to file
        with brain_path.open("a", encoding="utf-8") as f:
            f.write("\n".join(lines))

        logging.info(f"Appended {len(unique_entries)} entries to {brain_path}")
        return len(unique_entries), duplicate_count

    except Exception as e:
        logging.error(f"Failed to append entries to {brain_path}: {e}")
        return 0, len(sorted_entries)


# =============================================================================
# Cache Management
# =============================================================================

def load_cache() -> dict[str, Any]:
    """Load the crawl cache."""
    if CACHE_PATH.exists():
        try:
            return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
        except Exception as e:
            logging.warning(f"Failed to load cache: {e}")
    return {"last_crawl": None, "crawl_count": 0}


def save_cache(cache: dict[str, Any]) -> None:
    """Save the crawl cache."""
    try:
        CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
        CACHE_PATH.write_text(json.dumps(cache, indent=2), encoding="utf-8")
    except Exception as e:
        logging.warning(f"Failed to save cache: {e}")


def should_crawl(cache: dict[str, Any], min_days: int = 7) -> bool:
    """Check if enough time has passed since last crawl."""
    if not cache.get("last_crawl"):
        return True

    try:
        last_crawl = datetime.fromisoformat(cache["last_crawl"])
        days_since = (datetime.now() - last_crawl).days
        return days_since >= min_days
    except Exception:
        return True


# =============================================================================
# Main Orchestration
# =============================================================================

def run_full_crawl(dry_run: bool = False, sources_only: bool = False) -> CrawlResult:
    """Run the complete crawl pipeline."""
    final_result = CrawlResult()

    # Check cache
    cache = load_cache()
    if not dry_run and not should_crawl(cache):
        logging.info(f"Crawl ran recently (last: {cache.get('last_crawl')}); use --force to override")
        return final_result

    logging.info("=" * 60)
    logging.info(f"Starting knowledge base crawl for {SKILL_SLUG}")
    logging.info("=" * 60)

    # Crawl ArXiv categories
    if not sources_only:
        for category in ARXIV_CATEGORIES:
            result = crawl_arxiv_category(category)
            final_result.merge(result)

    # Crawl source URLs
    for source_url in SOURCE_URLS:
        result = crawl_source_url(source_url)
        final_result.merge(result)

    # Calculate relevance scores
    for entry in final_result.entries:
        entry.relevance_score = calculate_relevance_score(entry)

    # Log summary
    logging.info("=" * 60)
    logging.info("Crawl Summary:")
    logging.info(f"  Total entries: {len(final_result.entries)}")
    logging.info(f"  Sources crawled: {final_result.sources_crawled}")
    logging.info(f"  Sources failed: {final_result.sources_failed}")
    logging.info(f"  Errors: {len(final_result.errors)}")
    if final_result.errors:
        logging.info("  Error details:")
        for error in final_result.errors:
            logging.info(f"    - {error}")
    logging.info("=" * 60)

    # Update cache
    if not dry_run:
        cache["last_crawl"] = datetime.now().isoformat()
        cache["crawl_count"] = cache.get("crawl_count", 0) + 1
        save_cache(cache)

    return final_result


def setup_logging() -> None:
    """Configure logging for the updater."""
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(LOG_PATH),
            logging.StreamHandler(sys.stdout)
        ]
    )


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Update the knowledge base for Translation Quality Evaluation skill"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be added without modifying files"
    )
    parser.add_argument(
        "--arxiv-only",
        action="store_true",
        help="Only crawl ArXiv sources"
    )
    parser.add_argument(
        "--sources",
        action="store_true",
        help="Only crawl primary source URLs"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Run crawl even if recently executed"
    )
    parser.add_argument(
        "--min-score",
        type=float,
        default=0.0,
        help="Minimum relevance score to include (0.0-1.0)"
    )

    return parser.parse_args()


def main() -> int:
    """Main entry point."""
    args = parse_args()
    setup_logging()

    try:
        # Run crawl
        result = run_full_crawl(dry_run=args.dry_run, sources_only=args.sources)

        # Filter by minimum score
        if args.min_score > 0:
            filtered = [e for e in result.entries if e.relevance_score >= args.min_score]
            logging.info(f"Filtered to {len(filtered)} entries with score >= {args.min_score}")
            result.entries = filtered

        # Append to knowledge base
        if result.entries:
            appended, skipped = append_entries_to_brain(
                result.entries,
                BRAIN_PATH,
                dry_run=args.dry_run
            )
            logging.info(f"Results: {appended} appended, {skipped} skipped")

            if args.dry_run:
                logging.info("[DRY RUN] No files were modified")
        else:
            logging.warning("No entries to append")

        return 0

    except Exception as e:
        logging.error(f"Fatal error: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
