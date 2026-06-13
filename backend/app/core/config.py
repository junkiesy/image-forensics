from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]

DATASETS_DIR = PROJECT_ROOT / "datasets"
REAL_IMAGES_DIR = DATASETS_DIR / "real"
AI_IMAGES_DIR = DATASETS_DIR / "ai"

SUPPORTED_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}