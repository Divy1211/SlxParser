from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import u16, i16, u32

from smx.sections.smx_versions import DE_LATEST


class SmxLayerHeader(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    width: int =                  Retriever(u16,  default = 0)
    height: int =                 Retriever(u16,  default = 0)
    anchor_x: int =               Retriever(i16,  default = 0)
    anchor_y: int =               Retriever(i16,  default = 0)
    num_bytes: int =              Retriever(u32,  default = 0)
    num_bytes_uncompressed: int = Retriever(u32,  default = 0)
    # @formatter:on
