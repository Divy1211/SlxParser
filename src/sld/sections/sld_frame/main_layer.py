from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, ret
from bfp_rs.combinators import set_repeat, get_len, get
from bfp_rs.types.le import Array16, u8

from sld.sections.sld_frame.bc1_block import Bc1Block
from sld.sections.sld_frame.draw_command import SldDrawCommand
from sld.sections.sld_frame.layer_header import SldLayerHeader

from sld.sections.sld_versions import DE_LATEST

def set_pixel_data_repeats():
    num_bytes = get(ret(SldMainLayer.header), ret(SldLayerHeader.num_bytes))
    num_draw_commands = get_len(ret(SldMainLayer.draw_commands))

    total_num_bytes = num_bytes + ((4 - num_bytes) % 4)

    return [
        set_repeat(ret(SldMainLayer.pixels)).by((num_bytes - 2*num_draw_commands - 16)//8),
        set_repeat(ret(SldMainLayer._null)).by(total_num_bytes - num_bytes),
    ]


class SldMainLayer(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    header: SldLayerHeader =              Retriever(SldLayerHeader,          default_factory = SldLayerHeader)
    draw_commands: list[SldDrawCommand] = Retriever(Array16[SldDrawCommand], default_factory = lambda _ver: [], on_read = set_pixel_data_repeats)
    pixels: list[Bc1Block] =              Retriever(Bc1Block,                default_factory = Bc1Block, repeat = 0)
    _null: list[int] =                    Retriever(u8,                      default = 0, repeat = 0)
    # @formatter:on
