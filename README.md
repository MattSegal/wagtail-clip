# Wagtail CLIP

Wagtail CLIP allows you to search your Wagtail images using natural language queries.

_video here_

This project was inspired by, and draws heavily from [memery](https://github.com/deepfates/memery), by [deepfates](https://github.com/deepfates) et al.
It makes use of OpenAI's [CLIP model](https://github.com/openai/CLIP).

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

This package uses the

This packahe wraps the [CLIP model](https://github.com/openai/CLIP). which can be used for:

- encoding text into 1x512 float vectors
- encoding images into 1x512 float vectors

These vectors can be thought of as points in a 512 dimensional space, where the closer they are together, the more "related" they are.
Importantly, CLIP encodes both text and images into the _same_ space, meaning

## Contributing

If you want to help out, make a pull request and/or email me at `mattdsegal@gmail.com` or DM me on [Twitter](https://twitter.com/mattdsegal).
Probably better to talk to me first before writing a bunch of code.
