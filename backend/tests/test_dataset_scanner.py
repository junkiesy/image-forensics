from pathlib import Path

from app.services.dataset_scanner import count_images, list_image_files


def test_list_image_files_returns_only_supported_images(tmp_path: Path):
    supported_file = tmp_path / "image.jpg"
    unsupported_file = tmp_path / "notes.txt"

    supported_file.write_text("fake image content")
    unsupported_file.write_text("not an image")

    image_files = list_image_files(tmp_path)

    assert image_files == [supported_file]


def test_count_images_counts_supported_images(tmp_path: Path):
    (tmp_path / "one.png").write_text("fake")
    (tmp_path / "two.webp").write_text("fake")
    (tmp_path / "ignored.pdf").write_text("fake")

    assert count_images(tmp_path) == 2


def test_list_image_files_returns_empty_for_missing_directory(tmp_path: Path):
    missing_dir = tmp_path / "missing"

    assert list_image_files(missing_dir) == []