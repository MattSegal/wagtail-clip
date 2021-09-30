from setuptools import setup, find_packages
from os import path
from wagtailclip import __version__

here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md")) as f:
    long_description = f.read()


setup(
    name="wagtailclip",
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    description="Natural language search over Wagtail images.",
    long_description=long_description,
    url="https://github.com/mattsegal/wagtail-clip",
    author="Matthew Segal",
    author_email="mattdsegal@gmail.com",
    license="MIT",
    install_requires=[
        "wagtail>=2",
    ],
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Framework :: Django",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 2",
        "Topic :: Internet :: WWW/HTTP",
    ],
)