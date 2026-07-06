#!/usr/bin/env python3
"""Fetch a transcript for a YouTube video and save it as a plain-text file.

Maintainer helper for growing the skill's episode map: pull a new episode's
transcript, then distill it into `references/episode-map.md` (see MAINTAINING.md).

Usage:
    python scripts/youtube_transcript.py <url-or-id> -o transcripts/ep20_nazev.txt
    python scripts/youtube_transcript.py <url-or-id> --languages cs en

Requires: pip install -r requirements.txt  (youtube-transcript-api)
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Preferred caption languages, in order (auto-generated captions count too).
DEFAULT_LANGUAGES: tuple[str, ...] = ("cs", "en")

_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")
_URL_ID_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"(?:v=|/shorts/|/live/|/embed/|youtu\.be/)([A-Za-z0-9_-]{11})"),
)


def extract_video_id(url_or_id: str) -> str:
    """Return the 11-char video ID from a full YouTube URL or a bare ID.

    Raises ValueError if no valid ID can be found.
    """
    candidate = url_or_id.strip()
    if _ID_RE.match(candidate):
        return candidate
    for pattern in _URL_ID_PATTERNS:
        match = pattern.search(candidate)
        if match:
            return match.group(1)
    raise ValueError(f"Could not extract a YouTube video ID from: {url_or_id!r}")


def fetch_transcript_text(video_id: str, languages: tuple[str, ...]) -> str:
    """Fetch the transcript and return it as one joined text string.

    Supports both the modern (>=1.0) instance API and the legacy classmethod API
    of youtube-transcript-api, so it keeps working across versions.
    """
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError as exc:  # dependency not installed
        raise SystemExit(
            "Missing dependency. Run: pip install -r requirements.txt"
        ) from exc

    try:
        api = YouTubeTranscriptApi()
        fetched = api.fetch(video_id, languages=list(languages))
        return " ".join(snippet.text for snippet in fetched)
    except AttributeError:
        # Legacy API (<1.0): classmethod returning list of dicts.
        segments = YouTubeTranscriptApi.get_transcript(  # type: ignore[attr-defined]
            video_id, languages=list(languages)
        )
        return " ".join(segment["text"] for segment in segments)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", help="YouTube URL or 11-char video ID")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="File to write the transcript to (default: print to stdout)",
    )
    parser.add_argument(
        "--languages",
        nargs="+",
        default=list(DEFAULT_LANGUAGES),
        help=f"Preferred caption languages, in order (default: {' '.join(DEFAULT_LANGUAGES)})",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        video_id = extract_video_id(args.video)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    try:
        text = fetch_transcript_text(video_id, tuple(args.languages))
    except Exception as exc:  # surface the library's specific error to the user
        print(
            f"error: could not fetch transcript for {video_id}: "
            f"{type(exc).__name__}: {exc}",
            file=sys.stderr,
        )
        return 1

    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
        print(f"Wrote {len(text)} chars to {args.output}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
