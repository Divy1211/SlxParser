from __future__ import annotations

from typing import TYPE_CHECKING

from bfp_rs import BaseStruct, Retriever, Version, ret
from bfp_rs.combinators import set_repeat
from bfp_rs.types.le import (
    i16
)

from smx.sections.smx_frame import SmxFrame
from smx.sections.smx_header import SmxHeader
from smx.sections.smx_versions import DE_LATEST

if TYPE_CHECKING:
    from bfp_rs import ByteStream


class SmxFile(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    header: SmxHeader =      Retriever(SmxHeader, default_factory = SmxHeader, on_read = lambda: [set_repeat(ret(SmxFile.frames)).from_(ret(SmxFile.header), ret(SmxHeader.num_frames))])
    frames: list[SmxFrame] = Retriever(SmxFrame,  default_factory = lambda _ver: [], repeat = 0)
    # @formatter:on

    @classmethod
    def _get_version(
        cls,
        stream: ByteStream,
        _ver: Version = Version(0),
    ) -> Version:
        return Version(i16.from_bytes(stream.peek(6)[4:]))
