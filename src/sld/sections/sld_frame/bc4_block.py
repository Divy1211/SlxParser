from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import Array, u8

from sld.sections.sld_versions import DE_LATEST


class Bc4Block(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    color0: int =           Retriever(u8,           default = 0)
    color1: int =           Retriever(u8,           default = 0)
    pixel_data: list[int] = Retriever(Array[6][u8], default = 0)
    # @formatter:on
