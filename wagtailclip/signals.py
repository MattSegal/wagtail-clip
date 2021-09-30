import logging

from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image as PILImage

from .models import NaturalSearchImage, ImageEmbedding
from .encoder import encode_image

logger = logging.getLogger(__name__)


@receiver(post_save, sender=NaturalSearchImage)
def post_save_image(sender, instance, **kwargs):
    image = instance
    if image.file:
        try:
            # Try create an embedding for this file
            logger.info("Creating embedding for NaturalSearchImage<%s]>.", image.id)
            with image.file.storage.open(image.file.name, "rb") as f:
                # Read the file into a Pillow image
                pil_image = PILImage.open(f)
                # Encode Pillow image into a vector
                image_vec = encode_image(pil_image)

            # Store the vector (aka "embedding") in the database.
            ImageEmbedding.objects.update_or_create(
                image_id=image.id, defaults={"embedding": image_vec.tolist()}
            )
        except Exception:
            logger.exception(
                "Failed to create an embedding for NaturalSearchImage<%s]>.", image.id
            )
    else:
        logger.info(
            "No image found for NaturalSearchImage<%s]>, deleting all related embeddings.",
            image.id,
        )
        image.embeddings.all().delete()
