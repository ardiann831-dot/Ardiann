"""
Reference script for generating the 19 November World News infographic broadsheet
for the make.fun bounty (news-image-20261119).
"""

import json
from pathlib import Path

BOUNTY_ID = "news-image-20261119"
TARGET_DATE = "2026-11-19"

PROMPT = (
    'Dense editorial information broadsheet poster titled "19 NOVEMBER WORLD NEWS" '
    "with multiple interconnected news panels, diplomatic summit globes, financial "
    "market graphs, clean energy grid maps, maritime shipping lanes, space orbital "
    "tracks, and tech infrastructure diagrams, packed with crisp visual icons, data "
    "charts, regional badges, and structured callout boxes in a high-contrast modern "
    "infographic style."
)


def build_generation_config() -> dict:
    return {
        "bounty_id": BOUNTY_ID,
        "date": TARGET_DATE,
        "aspect_ratio": "3:4",
        "style": "high-density editorial infographic broadsheet",
        "prompt": PROMPT,
        "output_file": "output.jpg",
    }


if __name__ == "__main__":
    config = build_generation_config()
    Path("generation_config.json").write_text(
        json.dumps(config, indent=2), encoding="utf-8"
    )
    print(f"Saved generation configuration for {BOUNTY_ID} -> generation_config.json")