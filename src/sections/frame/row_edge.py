from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import u16

from sections.smx_versions import DE_LATEST


class RowEdge(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    padding_left: int =  Retriever(u16, default = 0)
    padding_right: int = Retriever(u16, default = 0)
    # @formatter:on
