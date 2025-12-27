from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import u8, u32

from smx.sections.smx_versions import DE_LATEST


class SmxFrameHeader(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    frame_type: int =        Retriever(u8,  default = 0x03)
    palette_number: int =    Retriever(u8,  default = 0)
    uncompressed_size: int = Retriever(u32, default = 0)
    # @formatter:on
