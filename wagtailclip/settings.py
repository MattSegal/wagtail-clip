from django.conf import settings

DOWNLOAD_PATH = getattr(settings, "WAGTAIL_CLIP_DOWNLOAD_PATH") or "/clip"
SEARCH_BACKEND_NAME = getattr(settings, "WAGTAIL_CLIP_SEARCH_BACKEND_NAME") or "clip"
MAX_IMAGE_SEARCH_RESULTS = (
    getattr(settings, "WAGTAIL_CLIP_MAX_IMAGE_SEARCH_RESULTS") or 256
)
