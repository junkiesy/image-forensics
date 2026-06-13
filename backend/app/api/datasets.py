from fastapi import APIRouter

from app.core.config import AI_IMAGES_DIR, REAL_IMAGES_DIR
from app.services.dataset_scanner import count_images

router = APIRouter(prefix="/datasets", tags=["datasets"])


@router.get("/summary")
def get_dataset_summary():
    return {
        "real_images": count_images(REAL_IMAGES_DIR),
        "ai_images": count_images(AI_IMAGES_DIR),
    }