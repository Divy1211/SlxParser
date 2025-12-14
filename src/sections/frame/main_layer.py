from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, ret
from bfp_rs.combinators import set_repeat
from bfp_rs.types.le import u32, u8

from sections.frame.layer_header import LayerHeader
from sections.frame.row_edge import RowEdge
from sections.smx_versions import DE_LATEST


class MainLayer(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    layer_header: LayerHeader = Retriever(LayerHeader, default_factory = LayerHeader, on_read = lambda: [set_repeat(ret(MainLayer.row_edges)).from_(ret(MainLayer.layer_header), ret(LayerHeader.height))])
    row_edges: list[RowEdge]  = Retriever(RowEdge,     default_factory = lambda _ver: [], repeat = 0)
    num_commands: int         = Retriever(u32,         default = 0, on_read = lambda: [set_repeat(ret(MainLayer.commands)).from_(ret(MainLayer.num_commands))])
    num_pixels: int           = Retriever(u32,         default = 0, on_read = lambda: [set_repeat(ret(MainLayer.pixels)).from_(ret(MainLayer.num_pixels))])
    commands: list[int]       = Retriever(u8,          default_factory = lambda _ver: [], repeat = 0)
    pixels: list[int]         = Retriever(u8,          default_factory = lambda _ver: [], repeat = 0)
    # @formatter:on
