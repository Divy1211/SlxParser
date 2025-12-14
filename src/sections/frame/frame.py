from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, ret
from bfp_rs.combinators import set_repeat, get, if_

from sections.frame.frame_header import FrameHeader
from sections.frame.main_layer import MainLayer
from sections.frame.outline_layer import OutlineLayer
from sections.frame.shadow_layer import ShadowLayer
from sections.smx_versions import DE_LATEST


def set_layer_repeats():
    main_bit = 0x1
    shadow_bit = 0x2
    outline_bit = 0x4

    frame_type = ret(Frame.frame_header), ret(FrameHeader.frame_type)
    return [
        if_(*frame_type).eq(get(*frame_type) & (~main_bit & 0xFF)).then(set_repeat(ret(Frame.main_layer)).to(-1)),
        if_(*frame_type).eq(get(*frame_type) & (~shadow_bit & 0xFF)).then(set_repeat(ret(Frame.shadow_layer)).to(-1)),
        if_(*frame_type).eq(get(*frame_type) & (~outline_bit & 0xFF)).then(set_repeat(ret(Frame.outline_layer)).to(-1)),
    ]


class Frame(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    frame_header: FrameHeader          = Retriever(FrameHeader,  default_factory = FrameHeader, on_read = set_layer_repeats)
    main_layer: MainLayer | None       = Retriever(MainLayer,    default_factory = MainLayer)
    shadow_layer: ShadowLayer | None   = Retriever(ShadowLayer,  default_factory = ShadowLayer)
    outline_layer: OutlineLayer | None = Retriever(OutlineLayer, default_factory = OutlineLayer)
    # @formatter:on
