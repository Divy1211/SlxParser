from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import u8, u16, i16

from sld.sections.sld_versions import DE_LATEST

class SldFrameHeader(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    width: int =      Retriever(u16,  default = 0)
    height: int =     Retriever(u16,  default = 0)
    anchor_x: int =   Retriever(i16,  default = 0)
    anchor_y: int =   Retriever(i16,  default = 0)
    frame_type: int = Retriever(u8,   default = 0x03)
    unknown: int =    Retriever(u8,   default = 0)
    index: int =      Retriever(u16,  default = 0)
    # @formatter:on
