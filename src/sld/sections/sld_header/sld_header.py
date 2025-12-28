from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import Str, i16, i32, u8, Array

from sld.sections.sld_versions import DE_LATEST


class SldHeader(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    signature: str =        Retriever(Str[4],        default = "SLDX")
    version: int =          Retriever(i16,           default = 4)
    num_frames: int =       Retriever(i16,           default = 0)
    flags: int =            Retriever(i16,           default = 0)
    num_bytes_header: int = Retriever(i16,           default = 16)
    global_alpha: int =     Retriever(u8,            default = 255)
    padding: int =          Retriever(Array[3][u8],  default_factory = lambda _ver: [0, 0, 0])
    # @formatter:on
