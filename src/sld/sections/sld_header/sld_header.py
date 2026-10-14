from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version, ByteStream
from bfp_rs.types.le import Str, i16, i32, u8, Array, u16

from sld.sections.sld_versions import DE_LATEST


class SldHeader(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    signature: str =        Retriever(Str[4],                    default = "SLDX")
    version: int =          Retriever(i16,                       default = 4)
    num_frames: int =       Retriever(i16,                       default = 0)
    flags: int =            Retriever(i16,                       default = 0)
    num_bytes_header: int = Retriever(i16,                       default = 16)
    global_alpha: int =     Retriever(u8,                        default = 255)
    _padding1: int =        Retriever(u8,                        default = 0)
    _padding2: int =        Retriever(u16, max_ver = Version(3), default = 0)
    # @formatter:on

    @classmethod
    def _get_version(cls, stream: ByteStream, ver = Version(0)):
        v = Version(i16.from_bytes(stream.peek(6)[4:]))
        print(v)
        return v
