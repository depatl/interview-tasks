#!/usr/bin/env python3
"""
fetch_hackernews.py

Script to read a configuration file (config.txt) that specifies how many top
Hacker News stories to retrieve. Then it calls the Hacker News API to fetch
the top stories, retrieves their details, and returns a JSON array.

Example output:
[
  {
    "id": 32417438,
    "title": "Some interesting article",
    "url": "https://some-domain.tld",
    "score": 128,
    "by": "alice"
  },
  ...
]

top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"

Usage:
    python fetch_hackernews.py
"""
