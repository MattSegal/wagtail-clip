from django.core.management.base import BaseCommand

from wagtailclip.encoder import load_model


class Command(BaseCommand):
    help = "Download CLIP model to disk"

    def handle(self, *args, **kwargs):
        load_model()
