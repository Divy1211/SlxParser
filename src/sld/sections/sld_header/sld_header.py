from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import Str, i16, i32

from sld.sections.sld_versions import DE_LATEST


class SldHeader(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    signature: str =      Retriever(Str[4],  default = "SLDX")
    version: int =        Retriever(i16,     default = 4)
    num_frames: int =     Retriever(i16,     default = 0)
    unknown1: int =       Retriever(i16,     default = 0)
    unknown2: int =       Retriever(i16,     default = 16)
    unknown3: int =       Retriever(i32,     default = 255)
    # @formatter:on
