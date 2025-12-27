from __future__ import annotations

from typing import TYPE_CHECKING

from bfp_rs import BaseStruct, Retriever, Version, ret
from bfp_rs.combinators import set_repeat
from bfp_rs.types.le import (
    i16
)

from sld.sections.sld_frame import SldFrame
from sld.sections.sld_header import SldHeader
from sld.sections.sld_versions import DE_LATEST

if TYPE_CHECKING:
    from bfp_rs import ByteStream


class SldFile(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    header: SldHeader =      Retriever(SldHeader, default_factory = SldHeader, on_read = lambda: [set_repeat(ret(SldFile.frames)).from_(ret(SldFile.header), ret(SldHeader.num_frames))])
    # frames: SldFrame  =      Retriever(SldFrame,  default_factory = SldFrame)
    frames: list[SldFrame] = Retriever(SldFrame,  default_factory = lambda _ver: [], repeat = 0)
    # @formatter:on

    @classmethod
    def _get_version(
        cls,
        stream: ByteStream,
        _ver: Version = Version(0),
    ) -> Version:
        return Version(i16.from_bytes(stream.peek(6)[4:]))
