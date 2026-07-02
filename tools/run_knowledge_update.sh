#!/bin/bash
# run_knowledge_update.sh - Wrapper script for knowledge_updater.py
# Usage: ./tools/run_knowledge_update.sh [options]
# Options: --dry-run, --arxiv-only, --sources, --force, --min-score=N

set -e

# Get the script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Change to project directory
cd "$PROJECT_DIR"

# Run the knowledge updater
python3 tools/knowledge_updater.py "$@"
