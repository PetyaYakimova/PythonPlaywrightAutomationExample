from pathlib import Path

# This file is in utils/, so go up one level to project root
PROJECT_ROOT = Path(__file__).resolve().parents[1]


def get_schema_path(name: str):
    return PROJECT_ROOT / "schemas" / name
