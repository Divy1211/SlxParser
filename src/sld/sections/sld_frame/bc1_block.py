from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import u16, Array, u8

from sld.sections.sld_versions import DE_LATEST


class Bc1Block(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    color0: int =           Retriever(u16, default = 0)
    color1: int =           Retriever(u16, default = 0)
    pixel_data: list[int] = Retriever(Array[4][u8], default = 0)
    # @formatter:on
