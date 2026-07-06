"""Tests for the pure URL/ID parsing in youtube_transcript.py."""

import pytest

from youtube_transcript import extract_video_id

VALID_ID = "dQw4w9WgXcQ"


@pytest.mark.parametrize(
    "value",
    [
        VALID_ID,
        f"https://www.youtube.com/watch?v={VALID_ID}",
        f"https://youtu.be/{VALID_ID}",
        f"https://www.youtube.com/watch?v={VALID_ID}&t=42s",
        f"https://www.youtube.com/live/{VALID_ID}",
        f"https://www.youtube.com/embed/{VALID_ID}",
        f"https://www.youtube.com/shorts/{VALID_ID}",
    ],
)
def test_extract_video_id_valid(value: str) -> None:
    assert extract_video_id(value) == VALID_ID


@pytest.mark.parametrize("value", ["", "not-a-url", "https://youtube.com/", "abc"])
def test_extract_video_id_invalid(value: str) -> None:
    with pytest.raises(ValueError):
        extract_video_id(value)
