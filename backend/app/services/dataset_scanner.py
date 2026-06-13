from pathlib import Path

from app.core.config import SUPPORTED_IMAGE_EXTENSIONS


def list_image_files(directory: Path) -> list[Path]:
    if not directory.exists():
        return []

    return sorted(
        [
            path
            for path in directory.iterdir()
            if path.is_file() and path.suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS
        ]
    )


def count_images(directory: Path) -> int:
    return len(list_image_files(directory))