from pathlib import Path


class Config:
    """Centralized project configuration."""

    PROJECT_ROOT = Path(__file__).resolve().parent.parent

    DATASETS = PROJECT_ROOT / "datasets"

    REPORTS = PROJECT_ROOT / "reports"

    SQL = PROJECT_ROOT / "sql"

    PIPELINES = PROJECT_ROOT / "pipelines"

    DOCS = PROJECT_ROOT / "docs"

    IMAGES = PROJECT_ROOT / "images"

    BRONZE = "Files/Bronze"

    SILVER = "Tables/Silver"

    GOLD = "Tables/Gold"