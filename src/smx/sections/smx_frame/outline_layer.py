from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, ret
from bfp_rs.combinators import set_repeat
from bfp_rs.types.le import Array32, u8

from smx.sections.smx_frame.layer_header import SmxLayerHeader
from smx.sections.smx_frame.row_edge import RowEdge
from smx.sections.smx_frame.shadow_layer import SmxShadowLayer
from smx.sections.smx_versions import DE_LATEST


class SmxOutlineLayer(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    header: SmxLayerHeader    = Retriever(SmxLayerHeader, default_factory = SmxLayerHeader, on_read = lambda: [set_repeat(ret(SmxOutlineLayer.row_edges)).from_(ret(SmxOutlineLayer.header), ret(SmxLayerHeader.height))])
    row_edges: list[RowEdge]  = Retriever(RowEdge,     default_factory = lambda _ver: [], repeat = 0)
    pixels: list[int]         = Retriever(Array32[u8], default_factory = lambda _ver: [])
    # @formatter:on
