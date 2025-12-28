from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, ret
from bfp_rs.combinators import set_repeat, get, if_

from sld.sections.sld_frame.damage_mask_layer import SldDamageMaskLayer
from sld.sections.sld_frame.frame_header import SldFrameHeader
from sld.sections.sld_frame.main_layer import SldMainLayer
from sld.sections.sld_frame.unused_layer import SldUnusedLayer
from sld.sections.sld_frame.player_color_mask_layer import SldPlayerColorMaskLayer
from sld.sections.sld_frame.shadow_layer import SldShadowLayer

from sld.sections.sld_versions import DE_LATEST


def set_layer_repeats():
    main_bit = 0x01
    shadow_bit = 0x02
    outline_bit = 0x04
    damage_mask_bit = 0x08
    player_color_mask_bit = 0x10

    frame_type = ret(SldFrame.header), ret(SldFrameHeader.frame_type)
    return [
        if_(*frame_type).eq(get(*frame_type) & (~main_bit & 0xFF)).then(set_repeat(ret(SldFrame.main_layer)).to(-1)),
        if_(*frame_type).eq(get(*frame_type) & (~shadow_bit & 0xFF)).then(set_repeat(ret(SldFrame.shadow_layer)).to(-1)),
        if_(*frame_type).eq(get(*frame_type) & (~outline_bit & 0xFF)).then(set_repeat(ret(SldFrame.unused_layer)).to(-1)),
        if_(*frame_type).eq(get(*frame_type) & (~damage_mask_bit & 0xFF)).then(set_repeat(ret(SldFrame.damage_mask_layer)).to(-1)),
        if_(*frame_type).eq(get(*frame_type) & (~player_color_mask_bit & 0xFF)).then(set_repeat(ret(SldFrame.player_color_mask_layer)).to(-1)),
    ]


class SldFrame(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    header: SldFrameHeader =                                  Retriever(SldFrameHeader,          default_factory = SldFrameHeader, on_read = set_layer_repeats)
    main_layer: SldMainLayer | None =                         Retriever(SldMainLayer,            default_factory = SldMainLayer)
    shadow_layer: SldShadowLayer | None =                     Retriever(SldShadowLayer,          default_factory = SldShadowLayer)
    unused_layer: SldUnusedLayer | None =                     Retriever(SldUnusedLayer,          default_factory = SldUnusedLayer)
    damage_mask_layer: SldDamageMaskLayer | None =            Retriever(SldDamageMaskLayer,      default_factory = SldDamageMaskLayer)
    player_color_mask_layer: SldPlayerColorMaskLayer | None = Retriever(SldPlayerColorMaskLayer, default_factory = SldPlayerColorMaskLayer)
    # @formatter:on
