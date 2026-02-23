#!/usr/bin/env python3
"""
BlackRoad Media — World Artifact RSS Feed Generator
Generates RSS and Atom feeds from AI-generated world artifacts.
"""
import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
import sqlite3

DB_PATH = Path.home() / ".blackroad" / "media-feed.db"


def _db() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("""
        CREATE TABLE IF NOT EXISTS feed_items (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            link TEXT,
            author TEXT DEFAULT "BlackRoad AI",
            published_at TEXT,
            tags TEXT,
            content_type TEXT DEFAULT "world-artifact"
        )
    """)
    conn.commit()
    return conn


def add_item(title: str, description: str, link: str = "",
             author: str = "BlackRoad AI", tags: str = "") -> str:
    item_id = hashlib.sha256(f"{title}{description}".encode()).hexdigest()[:12]
    with _db() as conn:
        conn.execute("""
            INSERT OR IGNORE INTO feed_items VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (item_id, title, description, link, author,
              datetime.now(timezone.utc).isoformat(), tags, "world-artifact"))
    return item_id


def generate_rss(limit: int = 50) -> str:
    """Generate RSS 2.0 feed XML."""
    with _db() as conn:
        items = conn.execute(
            "SELECT title, description, link, author, published_at, id FROM feed_items "
            "ORDER BY published_at DESC LIMIT ?", (limit,)
        ).fetchall()

    now = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")

    item_xml = ""
    for title, desc, link, author, pub, item_id in items:
        item_xml += f"""
  <item>
    <title>{_esc(title)}</title>
    <description>{_esc(desc or "")}</description>
    <link>{link or "https://blackroad.ai/worlds"}</link>
    <author>{_esc(author)}</author>
    <pubDate>{pub}</pubDate>
    <guid>blackroad-world-{item_id}</guid>
  </item>"""

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>BlackRoad World Artifacts</title>
    <link>https://blackroad.ai/worlds</link>
    <description>AI-generated world artifacts from the BlackRoad OS Pi fleet</description>
    <language>en-us</language>
    <lastBuildDate>{now}</lastBuildDate>
    <atom:link href="https://blackroad.ai/feed.xml" rel="self" type="application/rss+xml"/>
    {item_xml}
  </channel>
</rss>"""


def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def load_from_worlds_dir(worlds_dir: Path) -> int:
    """Load world artifact .md files into feed."""
    count = 0
    for md in sorted(worlds_dir.glob("*.md"), reverse=True)[:100]:
        text = md.read_text()
        lines = text.strip().split("\n")
        title = lines[0].lstrip("# ").strip() if lines else md.stem
        desc = " ".join(lines[1:4]).strip()[:280]
        add_item(title=title, description=desc, tags="world-artifact,ai-generated")
        count += 1
    return count


if __name__ == "__main__":
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"

    if cmd == "load" and len(sys.argv) > 2:
        n = load_from_worlds_dir(Path(sys.argv[2]))
        print(f"✅ Loaded {n} world artifacts")

    elif cmd == "rss":
        out = Path("dist/feed.xml")
        out.parent.mkdir(exist_ok=True)
        out.write_text(generate_rss())
        print(f"✅ RSS feed written to {out}")

    elif cmd == "add":
        item_id = add_item(title=sys.argv[2], description=sys.argv[3] if len(sys.argv) > 3 else "")
        print(f"✅ Added item: {item_id}")

    else:
        print("Usage: python rss_feed.py [load <worlds-dir> | rss | add <title> [desc]]")

