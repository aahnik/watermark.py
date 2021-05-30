# watermark.py

![PyPI](https://img.shields.io/pypi/v/watermark.py)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/watermark.py)

A convenient python wrapper around FFmpeg to apply watermarks to images, gifs,
and videos.

## Installation

```shell
pip install watermark.py
```

You need to install  [`ffmpeg`](https://ffmpeg.org/) seperately.

## Usage

```python
from watermark import File, Watermark, apply_watermark, Position

video = File("vid.mp4")
watermark = Watermark(File("im.png"), pos=Position.bottom_right)

apply_watermark(video, watermark)
```

## Used by

- [telewater](https://github.com/aahnik/telewater)
A telegram bot that applies watermark on images, gifs, and videos.
