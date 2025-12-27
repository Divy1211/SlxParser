from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, ret
from bfp_rs.combinators import set_repeat
from bfp_rs.types.le import u32, u8

from smx.sections.smx_frame.layer_header import SmxLayerHeader
from smx.sections.smx_frame.row_edge import RowEdge
from smx.sections.smx_versions import DE_LATEST


class SmxMainLayer(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    header: SmxLayerHeader    = Retriever(SmxLayerHeader, default_factory = SmxLayerHeader, on_read = lambda: [set_repeat(ret(SmxMainLayer.row_edges)).from_(ret(SmxMainLayer.header), ret(SmxLayerHeader.height))])
    row_edges: list[RowEdge]  = Retriever(RowEdge,     default_factory = lambda _ver: [], repeat = 0)
    num_commands: int         = Retriever(u32,         default = 0, on_read = lambda: [set_repeat(ret(SmxMainLayer.commands)).from_(ret(SmxMainLayer.num_commands))])
    num_pixels: int           = Retriever(u32,         default = 0, on_read = lambda: [set_repeat(ret(SmxMainLayer.pixels)).from_(ret(SmxMainLayer.num_pixels))])
    commands: list[int]       = Retriever(u8,          default = 0, repeat = 0)
    pixels: list[int]         = Retriever(u8,          default = 0, repeat = 0)
    # @formatter:on
