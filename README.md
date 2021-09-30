# Wagtail CLIP

https://github.com/deepfates/memery/tree/main/

git@github.com:MattSegal/wagtail-clip.git
git@github.com:MattSegal/wagtail-clip-example.git

## Installation

You can install this repository as follows:

```bash
pip install \
    wagtailclip@git+https://github.com/MattSegal/wagtail-clip.git \
    -f https://download.pytorch.org/whl/torch_stable.html \
    torch==1.7.1+cpu \
    torchvision==0.8.2+cpu
```

You will find that this installs ~200MB of deep learning libraries (PyTorch).

Settings

```python

INSTALLED_APPS = [
    # ... whatever ...
    "wagtailclip",
]

WAGTAIL_CLIP_DOWNLOAD_PATH = "/clip"
WAGTAIL_CLIP_SEARCH_BACKEND_NAME = "clip"
WAGTAIL_CLIP_MAX_IMAGE_SEARCH_RESULTS = 256
WAGTAILIMAGES_IMAGE_MODEL = "wagtailclip.NaturalSearchImage"
WAGTAILSEARCH_BACKENDS = {
    # ... whatever ...
    "clip": {
        "BACKEND": "wagtailclip.search.CLIPSearchBackend",
    },
}
```

Yo

```bash
./manage.py download_clip
```

## Tradeoffs

pros

- natural language image search
- image similarity search

cons

- torch dependency (~200MB of deep learning libraries)
- CLIP dependency (~340MB of model parameters)

## How it works

pass

## Example project

pass

## Contributions

pass
