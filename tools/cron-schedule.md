# Cron Schedule Configuration for Knowledge Updater

This document provides cron schedule configuration for automated weekly updates of the SECOND-KNOWLEDGE-BRAIN.md knowledge base.

## Cron Job Configuration

### Standard Weekly Schedule (Recommended)

Run every Sunday at 02:00 UTC (low-traffic time):

```cron
# Translation Quality Evaluation - Knowledge Base Updater
# Runs weekly on Sunday at 02:00 UTC
0 2 * * 0 cd /path/to/skills/translation-quality-evaluation && /usr/bin/python3 tools/knowledge_updater.py >> logs/cron.log 2>&1
```

### Alternative Schedules

**Daily early morning:**
```cron
0 2 * * * cd /path/to/skills/translation-quality-evaluation && /usr/bin/python3 tools/knowledge_updater.py >> logs/cron.log 2>&1
```

**Twice weekly (Sunday and Wednesday):**
```cron
0 2 * * 0,3 cd /path/to/skills/translation-quality-evaluation && /usr/bin/python3 tools/knowledge_updater.py >> logs/cron.log 2>&1
```

**Weekly on Monday (alternative to Sunday):**
```cron
0 2 * * 1 cd /path/to/skills/translation-quality-evaluation && /usr/bin/python3 tools/knowledge_updater.py >> logs/cron.log 2>&1
```

## Installation Instructions

### Linux/macOS (crontab)

1. Edit crontab:
```bash
crontab -e
```

2. Add the cron job (replace `/path/to/skills` with actual path):
```cron
# Translation Quality Evaluation - Knowledge Base Updater
0 2 * * 0 cd /path/to/skills/translation-quality-evaluation && /usr/bin/python3 tools/knowledge_updater.py >> logs/cron.log 2>&1
```

3. Save and exit

4. Verify cron job installed:
```bash
crontab -l | grep knowledge_updater
```

### Using /etc/cron.d/ (System-wide)

Create `/etc/cron.d/translation-quality-eval`:
```cron
# Translation Quality Evaluation - Knowledge Base Updater
# Runs weekly on Sunday at 02:00 UTC
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
0 2 * * 0 root cd /path/to/skills/translation-quality-evaluation && /usr/bin/python3 tools/knowledge_updater.py >> /path/to/skills/translation-quality-evaluation/logs/cron.log 2>&1
```

Set permissions:
```bash
sudo chmod 644 /etc/cron.d/translation-quality-eval
```

### systemd Timer (Alternative to cron)

Create `/etc/systemd/system/translation-quality-eval-updater.service`:
```ini
[Unit]
Description=Translation Quality Evaluation Knowledge Base Updater
After=network-online.target

[Service]
Type=oneshot
User=root
WorkingDirectory=/path/to/skills/translation-quality-evaluation
ExecStart=/usr/bin/python3 tools/knowledge_updater.py
StandardOutput=append:/path/to/skills/translation-quality-evaluation/logs/cron.log
StandardError=append:/path/to/skills/translation-quality-evaluation/logs/cron.log
```

Create `/etc/systemd/system/translation-quality-eval-updater.timer`:
```ini
[Unit]
Description=Weekly Translation Quality Evaluation Knowledge Base Update
Requires=translation-quality-eval-updater.service

[Timer]
OnCalendar=Sun *-*-* 02:00:00 UTC
Persistent=true

[Install]
WantedBy=timers.target
```

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable translation-quality-eval-updater.timer
sudo systemctl start translation-quality-eval-updater.timer
```

Check status:
```bash
systemctl status translation-quality-eval-updater.timer
systemctl list-timers | grep translation-quality
```

### Windows Task Scheduler

1. Open Task Scheduler
2. Create Basic Task
3. Name: "Translation Quality Eval Knowledge Updater"
4. Trigger: Weekly on Sunday at 2:00 AM
5. Action: Start a program
   - Program: `python.exe`
   - Arguments: `D:\skills\translation-quality-evaluation\tools\knowledge_updater.py`
   - Start in: `D:\skills\translation-quality-evaluation`

## Monitoring and Logging

### Log Files

Logs are written to:
- `logs/knowledge_updater.log` - Detailed crawl logs
- `logs/cron.log` - Cron execution output

### Check Recent Runs

```bash
# Last 10 lines
tail -n 10 logs/knowledge_updater.log

# Last 20 lines with timestamps
tail -n 20 -f logs/knowledge_updater.log

# Search for errors
grep ERROR logs/knowledge_updater.log

# Count entries added this week
grep "New entries added" logs/knowledge_updater.log | tail -n 1
```

### Manual Run for Testing

```bash
# Dry run to see what would be added
cd /path/to/skills/translation-quality-evaluation
python3 tools/knowledge_updater.py --dry-run

# Full run
python3 tools/knowledge_updater.py

# Run with minimum relevance score
python3 tools/knowledge_updater.py --min-score 0.3
```

## Dependencies

Required Python packages:
```bash
pip install crawl4ai beautifulsoup4 requests
```

System requirements:
- Python 3.8+
- Internet connectivity
- Write access to skill directory

## Troubleshooting

### Cron job not running

Check cron service:
```bash
# Linux
sudo systemctl status cron

# macOS
sudo launchctl list | grep cron
```

Verify cron syntax:
```bash
# Check crontab
crontab -l

# Test cron time (shows next run times)
crontab -l | crontab-
```

### Python not found

Use absolute path to Python:
```bash
which python3  # Linux/macOS
where python   # Windows
```

Update cron job with absolute path:
```cron
0 2 * * 0 cd /path/to/skills/translation-quality-evaluation && /usr/local/bin/python3 tools/knowledge_updater.py >> logs/cron.log 2>&1
```

### Permission denied

Ensure write permissions:
```bash
chmod +x tools/knowledge_updater.py
chmod -R +w logs/ .cache/
```

### crawl4ai import error

Install dependencies:
```bash
pip install crawl4ai beautifulsoup4 requests
```

Or use virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install crawl4ai beautifulsoup4 requests
```

Update cron to use virtual environment:
```cron
0 2 * * 0 cd /path/to/skills/translation-quality-evaluation && /path/to/venv/bin/python tools/knowledge_updater.py >> logs/cron.log 2>&1
```

### No new entries added

Check sources are accessible:
```bash
curl -I https://www.taus.net/resources
curl -I https://arxiv.org/list/cs.CL/recent
```

Check relevance scoring:
```bash
python3 tools/knowledge_updater.py --min-score 0.1
```

## Verification

After installation, verify the cron job:

1. **Check cron is scheduled:**
```bash
crontab -l | grep knowledge_updater
```

2. **Wait for next scheduled run or run manually:**
```bash
cd /path/to/skills/translation-quality-evaluation
python3 tools/knowledge_updater.py
```

3. **Check logs:**
```bash
tail -n 20 logs/knowledge_updater.log
```

4. **Verify knowledge base updated:**
```bash
tail -n 50 SECOND-KNOWLEDGE-BRAIN.md | grep "Automated Crawl Batch"
```

## Maintenance

### Monthly: Review crawl results

```bash
# Check entries added this month
grep "Automated Crawl Batch" SECOND-KNOWLEDGE-BRAIN.md | grep $(date +%Y-%m)
```

### Quarterly: Update source lists

Edit `tools/knowledge_updater.py`:
- Update `SEARCH_QUERIES` for new research areas
- Update `SOURCE_URLS` for new authoritative sources
- Update `DOMAIN_KEYWORDS` for expanded terminology

### Annually: Review and prune

- Remove outdated or superseded entries
- Consolidate redundant entries
- Update framework descriptions if standards change

## Security Considerations

1. **File Permissions:** Ensure logs and cache are not world-writable
```bash
chmod 750 logs/
chmod 640 logs/*.log
```

2. **Network Security:** The tool only reads from HTTPS sources

3. **Input Validation:** All inputs are validated before processing

4. **Rate Limiting:** Built-in delays between requests to avoid overwhelming sources

## Advanced Configuration

### Custom Schedule

Run at specific times based on your timezone:

```cron
# Example: Every Monday at 9:00 AM Pacific
0 9 * * 1 TZ='America/Los_Angeles' cd /path/to/skills/translation-quality-evaluation && /usr/bin/python3 tools/knowledge_updater.py >> logs/cron.log 2>&1
```

### Conditional Execution

Only run if file is older than 7 days:
```cron
0 2 * * 0 [ $(find /path/to/skills/translation-quality-evaluation/SECOND-KNOWLEDGE-BRAIN.md -mtime +7) ] && cd /path/to/skills/translation-quality-evaluation && /usr/bin/python3 tools/knowledge_updater.py >> logs/cron.log 2>&1
```

### Email Notifications

Add email notification on failure:
```cron
0 2 * * 0 cd /path/to/skills/translation-quality-evaluation && /usr/bin/python3 tools/knowledge_updater.py >> logs/cron.log 2>&1 || mail -s "Knowledge Update Failed" admin@example.com < logs/cron.log
```

## Support

For issues or questions:
- Check logs: `logs/knowledge_updater.log`
- Run dry-run: `python3 tools/knowledge_updater.py --dry-run`
- Review this document
- Check crawl4ai documentation: https://github.com/unclecode/crawl4ai

---

**Last Updated:** 2026-07-02
**Cron Version:** 1.0.0
