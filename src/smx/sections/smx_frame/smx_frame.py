from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, ret
from bfp_rs.combinators import set_repeat, get, if_

from smx.sections.smx_frame.frame_header import SmxFrameHeader
from smx.sections.smx_frame.main_layer import SmxMainLayer
from smx.sections.smx_frame.outline_layer import SmxOutlineLayer
from smx.sections.smx_frame.shadow_layer import SmxShadowLayer

from smx.sections.smx_versions import DE_LATEST


def set_layer_repeats():
    main_bit = 0x1
    shadow_bit = 0x2
    outline_bit = 0x4

    frame_type = ret(SmxFrame.header), ret(SmxFrameHeader.frame_type)
    return [
        if_(*frame_type).eq(get(*frame_type) & (~main_bit & 0xFF)).then(set_repeat(ret(SmxFrame.main_layer)).to(-1)),
        if_(*frame_type).eq(get(*frame_type) & (~shadow_bit & 0xFF)).then(set_repeat(ret(SmxFrame.shadow_layer)).to(-1)),
        if_(*frame_type).eq(get(*frame_type) & (~outline_bit & 0xFF)).then(set_repeat(ret(SmxFrame.outline_layer)).to(-1)),
    ]


class SmxFrame(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    header: SmxFrameHeader                = Retriever(SmxFrameHeader,  default_factory = SmxFrameHeader, on_read = set_layer_repeats)
    main_layer: SmxMainLayer | None       = Retriever(SmxMainLayer,    default_factory = SmxMainLayer)
    shadow_layer: SmxShadowLayer | None   = Retriever(SmxShadowLayer,  default_factory = SmxShadowLayer)
    outline_layer: SmxOutlineLayer | None = Retriever(SmxOutlineLayer, default_factory = SmxOutlineLayer)
    # @formatter:on
