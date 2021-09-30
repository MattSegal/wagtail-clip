import functools

import clip
import torch
from PIL import Image as PILImage

from .settings import DOWNLOAD_PATH


@functools.lru_cache(maxsize=1)
def load_model():
    """
    Load CLIP model into memory.
    Will download the model from the internet if it's not found in `WAGTAIL_MEMERY_CLIP_DOWNLOAD_PATH`.
    """
    device = torch.device("cpu")
    model, preprocess = clip.load("ViT-B/32", device, download_root=DOWNLOAD_PATH)
    return model, device, preprocess


def encode_text(text: str) -> torch.FloatTensor:
    """
    Returns a 512 element vector text query embedding.
    """
    model, device, _ = load_model()
    with torch.no_grad():
        # Tokenise the text
        text = clip.tokenize(text).to(device)
        # Encode the text as a vector.
        text_features = model.encode_text(text).squeeze(0)
        # Normalise the vector.
        text_features = text_features / text_features.norm(dim=-1, keepdim=True)

    return text_features


def encode_image(image: PILImage) -> torch.FloatTensor:
    """
    Returns a 512 element vector image embedding.
    """
    model, device, preprocess = load_model()
    with torch.no_grad():
        # Preprocess the image
        image_preprocessed = preprocess(image).unsqueeze(0).to(device)
        # Encode the image as a vector.
        image_features = model.encode_image(image_preprocessed).squeeze(0)
        # Normalise the vector.
        image_features = image_features / image_features.norm(dim=-1, keepdim=True)

    return image_features
