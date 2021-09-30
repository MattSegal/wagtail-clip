from django.db import models
from django.contrib.postgres.fields import ArrayField
from wagtail.images.models import Image
from wagtail.search.queryset import SearchableQuerySetMixin

from .settings import SEARCH_BACKEND_NAME


class ImageQuerySet(SearchableQuerySetMixin, models.QuerySet):
    def search(self, *args, **kwargs):
        return super().search(*args, **kwargs, backend=SEARCH_BACKEND_NAME)


class NaturalSearchImage(Image):
    objects = ImageQuerySet.as_manager()


class ImageEmbedding(models.Model):
    embedding = ArrayField(models.FloatField(), size=512)
    image = models.ForeignKey(
        NaturalSearchImage, on_delete=models.CASCADE, related_name="embeddings"
    )
