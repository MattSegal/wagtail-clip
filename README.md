# Wagtail CLIP

Wagtail CLIP allows you to search your Wagtail images using natural language queries.

<iframe width="640" height="529" src="https://www.loom.com/embed/61b7bb81cd4f436b842a32befe7f0b35" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

This project was inspired by, and draws heavily from [memery](https://github.com/deepfates/memery), by [deepfates](https://github.com/deepfates) et al.
It makes use of OpenAI's [CLIP model](https://github.com/openai/CLIP) (it was very nice of them to open source it, cheers).

[An example project is available here](https://github.com/MattSegal/wagtail-clip-example)

## Installation

You can install this package as follows (requires Git):

```bash
pip install \
    wagtailclip@git+https://github.com/MattSegal/wagtail-clip.git \
    -f https://download.pytorch.org/whl/torch_stable.html \
    torch==1.7.1+cpu \
    torchvision==0.8.2+cpu
```

You will find that this installs ~200MB of deep learning libraries (PyTorch). You will also need to update your Django project's settings:

```python

INSTALLED_APPS = [
    # ... whatever ...
    "wagtailclip",
]

# A place to store ~330MB of downloaded model parameters
WAGTAIL_CLIP_DOWNLOAD_PATH = "/clip"
# Maximum number of search results
WAGTAIL_CLIP_MAX_IMAGE_SEARCH_RESULTS = 256
# A unique name for the search backend.
WAGTAIL_CLIP_SEARCH_BACKEND_NAME = "clip"
# Recommended model, or your can roll your own (read the source).
WAGTAILIMAGES_IMAGE_MODEL = "wagtailclip.NaturalSearchImage"
# Add the search backend.
WAGTAILSEARCH_BACKENDS = {
    # ... whatever ...
    WAGTAIL_CLIP_SEARCH_BACKEND_NAME: {
        "BACKEND": "wagtailclip.search.CLIPSearchBackend",
    },
}
```

That's enough to get started, however if you want pre-download the ~330MB of model parameters, you can run this management command:

```bash
./manage.py download_clip
```

## How it works

This package wraps the [CLIP model](https://github.com/openai/CLIP). which can be used for:

- encoding text into 1x512 float vectors
- encoding images into 1x512 float vectors

These vectors can be thought of as points in a 512 dimensional space, where the closer two points are to each other, the more "related" they are.
Importantly, CLIP encodes both text and images into the _same_ space, meaning that we can:

- encode all Wagtail images into vectors and store them in the database
- encode a user's search query text into a vector; and then
- compare the search query vector with all the image vectors

This comparison is done using a dot product to get a similarity score for each image. The operation is performed in Python.
Once we have a similarity score we pick the top N (say, 256) most similar images and return those as the results.

## Will this scale?

Haha probably not. I've tested my naive implementation on up to 2048 images and it runs OK (~3s / query).
There are specialized Postgres extensions and vector similarity databases that you can use if you want to do this for tens of thousands of images.

## Contributing

If you want to help out, make a pull request and/or email me at `mattdsegal@gmail.com` or DM me on [Twitter](https://twitter.com/mattdsegal).
Probably better to talk to me first before writing a bunch of code.
