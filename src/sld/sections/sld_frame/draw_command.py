from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import u8

from sld.sections.sld_versions import DE_LATEST


class SldDrawCommand(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    skipped_block_count: int = Retriever(u8, default = 0)
    draw_block_count: int    = Retriever(u8, default = 0)
    # @formatter:on
