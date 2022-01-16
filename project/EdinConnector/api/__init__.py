from fastapi import APIRouter
from .documents import router as doc_router


router =APIRouter()
router.include_router(doc_router)
