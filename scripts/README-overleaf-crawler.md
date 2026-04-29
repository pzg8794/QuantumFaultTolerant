# Overleaf Feedback Crawler

This is a small **read-only** Playwright crawler for collecting visible Overleaf review/comment-panel feedback into structured files.

It is not an official Overleaf API client. It uses a local browser session, so credentials are not stored in the repository. Run it while logged into Overleaf.

## Files

- `scripts/crawl_overleaf_feedback.py` — crawler
- `scripts/requirements-overleaf-crawler.txt` — Python dependency list
- `feedback/overleaf_feedback_raw.json` — generated raw structured output
- `feedback/overleaf_feedback_queue.md` — generated Markdown queue for review workflow

The generated `feedback/overleaf_feedback_raw.json` file and local browser auth directory are ignored by Git.

## Setup

```bash
/Users/pitergarcia/DataScience/Semester4/GA-Work/.quantum/bin/python -m pip install -r scripts/requirements-overleaf-crawler.txt
/Users/pitergarcia/DataScience/Semester4/GA-Work/.quantum/bin/python -m playwright install chromium
```

## Run

```bash
/Users/pitergarcia/DataScience/Semester4/GA-Work/.quantum/bin/python scripts/crawl_overleaf_feedback.py \
  --project-url https://www.overleaf.com/project/68ea344896594f27b427ca8f \
  --out-json feedback/overleaf_feedback_raw.json \
  --out-md feedback/overleaf_feedback_queue.md \
  --pause-before-scrape
```

The browser opens visibly by default. If Overleaf asks you to log in, log in in the browser window, open the review/comment panel, then return to the terminal and press Enter.

## Output workflow

The Markdown output follows the paper-review workflow:

1. Feedback
2. Task
3. Content in question
4. Proposed solution / new content
5. Evaluation of solution
6. Decision / applied modification

The script attempts to capture selected or active editor text as the content in question. Treat matches as candidates and verify before applying manuscript edits.

## Safety

The crawler does not resolve comments, reply to comments, delete comments, edit source, accept tracked changes, or push to Overleaf. It only reads visible DOM text and writes local output files.

## Troubleshooting

If no feedback items are found:

```bash
python scripts/crawl_overleaf_feedback.py --pause-before-scrape --slow-mo 100
```

Then manually open the review/comment sidebar in the browser before pressing Enter.
