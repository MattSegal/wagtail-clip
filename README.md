# Wagtail CLIP

https://github.com/deepfates/memery/tree/main/

git@github.com:MattSegal/wagtail-clip.git
git@github.com:MattSegal/wagtail-clip-example.git

## Installation

```bash
pip install wagtail-clip
```

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

```bash
./manage.py download_clip
```

## Tradeoffs

pros

- natural language image search
- image similarity search

cons

- torch dependency (~1.2GB of env (recheck))
- CLIP dependency (~340MB of model parameters)

## How it works

pass

## Example project

pass

## Contributions

pass
