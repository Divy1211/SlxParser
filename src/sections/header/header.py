from __future__ import annotations

from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import Str, i16, i32

from sections.smx_versions import DE_LATEST


class Header(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    signature: str =      Retriever(Str[4],  default = "SMPX")
    version: int =        Retriever(i16,     default = 2)
    num_frames: int =     Retriever(i16,     default = 0)
    file_size_smx: int =  Retriever(i32,     default = 0)
    file_size_smp: int =  Retriever(i32,     default = 0)
    comment: str =        Retriever(Str[16], default = "v0.1.0 SmxParser")
    # @formatter:on
