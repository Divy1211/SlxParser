from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import u16, i16, u32, u8

from smx.sections.smx_versions import DE_LATEST


class SldLayerHeader(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    num_bytes: int =    Retriever(u32,  default = 0)
    offset_x1: int =    Retriever(u16,  default = 0)
    """top left"""
    offset_y1: int =    Retriever(u16,  default = 0)
    """top left"""
    offset_x2: int =    Retriever(u16,  default = 0)
    """bottom right"""
    offset_y2: int =    Retriever(u16,  default = 0)
    """bottom right"""
    flag1: int =        Retriever(u8,   default = 0)
    unknown: int =      Retriever(u8,   default = 1)
    # @formatter:on
