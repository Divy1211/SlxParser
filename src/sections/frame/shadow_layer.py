from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, ret
from bfp_rs.combinators import set_repeat
from bfp_rs.types.le import Array32, u8

from sections.frame.layer_header import LayerHeader
from sections.frame.row_edge import RowEdge
from sections.smx_versions import DE_LATEST


class ShadowLayer(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    layer_header: LayerHeader = Retriever(LayerHeader, default_factory = LayerHeader, on_read = lambda: [set_repeat(ret(ShadowLayer.row_edges)).from_(ret(ShadowLayer.layer_header), ret(LayerHeader.height))])
    row_edges: list[RowEdge]  = Retriever(RowEdge,     default_factory = lambda _ver: [], repeat = 0)
    pixels: list[int]         = Retriever(Array32[u8], default_factory = lambda _ver: [])
    # @formatter:on
