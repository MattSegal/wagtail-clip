import logging
from time import time

import torch
from wagtail.search.backends.base import BaseSearchBackend

from .models import NaturalSearchImage, ImageEmbedding
from .encoder import encode_text
from .settings import MAX_IMAGE_SEARCH_RESULTS

logger = logging.getLogger(__name__)


class CLIPSearchBackend(BaseSearchBackend):
    def autocomplete(self, query, *args, **kwargs):
        # I don't really know what this does.
        return NaturalSearchImage.objects.none()

    def search(self, query, *args, **kwargs):
        with Timer("Searching images"):
            with Timer("Encoding text query"):
                # Get the text vector.
                query_vec = encode_text(query)

            with Timer("Calculating cosine distance"):
                # Compare the query vec to every image embedding and rank by similarity.
                # This is faster than trying to calculate this in a DB query as far as I can tell.
                ie_qs = ImageEmbedding.objects.values_list("image_id", "embedding")
                image_ids, embeddings = [[i for i, _ in ie_qs], [j for _, j in ie_qs]]
                embeddings = torch.FloatTensor(embeddings)
                max_search_results = min(len(image_ids), MAX_IMAGE_SEARCH_RESULTS)
                dot_product = torch.sum(query_vec * embeddings, dim=-1)
                _, top_k_idxs = torch.topk(dot_product, k=max_search_results)
                pk_list = [image_ids[idx] for idx in top_k_idxs]

            # Return images in order of ranked embeddings.
            # FIXME: Surely there's a better way to do this.
            clauses = " ".join(
                ["WHEN id=%s THEN %s" % (pk, i) for i, pk in enumerate(pk_list)]
            )
            ordering = "CASE %s END" % clauses
            return NaturalSearchImage.objects.filter(pk__in=pk_list).extra(
                select={"ordering": ordering}, order_by=("ordering",)
            )


class Timer:
    """Prints the time that a block of code takes to run"""

    def __init__(self, message):
        self.message = message
        self.start = None

    def __enter__(self):
        self.start = time()
        msg = self.message[0].upper() + self.message[1:]
        logger.debug(f"{msg}...")

    def __exit__(self, *args):
        runtime = time() - self.start
        msg = self.message[0].lower() + self.message[1:]
        logger.debug(f"Finished {msg} in {runtime:0.1f} seconds.")
