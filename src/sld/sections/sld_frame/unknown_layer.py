from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, ret
from bfp_rs.combinators import set_repeat, get, get_len
from bfp_rs.types.le import u8, u32

from sld.sections.sld_versions import DE_LATEST

def set_data_repeats():
    num_bytes = get(ret(SldUnknownLayer.num_bytes))
    total_num_bytes = num_bytes + ((4 - num_bytes) % 4)

    return [
        set_repeat(ret(SldUnknownLayer.data)).by(get(SldUnknownLayer.num_bytes) - 4),
        set_repeat(ret(SldUnknownLayer._null)).by(total_num_bytes - num_bytes),
    ]

class SldUnknownLayer(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    num_bytes: int =   Retriever(u32, default = 0, on_read = set_data_repeats)
    data: list[int] =  Retriever(u8,  default = 0, repeat = 0)
    _null: list[int] = Retriever(u8,  default = 0, repeat = 0)
    # @formatter:on
