from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import u32, u8

from smx.sections.smx_versions import DE_LATEST


class SldShortLayerHeader(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    num_bytes: int =      Retriever(u32,  default = 0)
    storage_scheme: int = Retriever(u8,   default = 0)
    padding: int =        Retriever(u8,   default = 1)
    # @formatter:on
