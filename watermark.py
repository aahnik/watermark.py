#!/usr/bin/env python

# MIT License
# Copyright (c) 2021 Aahnik Daw

import os
from enum import Enum
from mimetypes import guess_type


class Position(str, Enum):
    top_left = "top_left"
    top_right = "top_right"
    centre = "centre"
    bottom_left = "bottom_left"
    bottom_right = "bottom_right"


offset_map = {
    "top_left": "10:10",
    "top_right": "W-w-10:10",
    "centre": "(W-w)/2:(H-h)/2",
    "bottom_left": "10:H-h-10",
    "bottom_right": "W-w-10:H-h-10",
}


class File:
    def __init__(self, path: str) -> None:
        if not os.path.isfile(path):
            raise FileNotFoundError(f"File {path} does not exist.")
        self.path = path
        self.type = self.find_type()

    def find_type(self) -> str:
        _type = guess_type(self.path)[0]
        if not _type:
            raise Exception(f"File type cant be recognized")

        _type = _type.split("/")[0]
        if _type in ["image", "video"]:
            return _type
        else:
            raise ValueError(f"Type {_type} is not supported.")


class Watermark:
    def __init__(
        self,
        overlay: File,
        pos: Position = Position.centre,
        offset: str = "",
    ) -> None:
        self.overlay = overlay
        self.pos = pos
        if not offset:
            offset = offset_map.get(self.pos)
        self.offset = offset


def apply_watermark(
    file: File,
    wtm: Watermark,
    output_file: str = "",
    frame_rate: int = 15,
    preset: str = "ultrafast",
) -> str:

    if not output_file:
        output_file = f"watered_{file.path}"
    command = f'ffmpeg -i {file.path} \
        -i {wtm.overlay.path} \
        -an -dn -sn -r {frame_rate} \
        -preset {preset} \
        -tune zerolatency  -tune fastdecode \
        -filter_complex "overlay={wtm.offset}" \
        {output_file}'

    print(f"Running command {command}")
    os.system(command)
    return output_file
