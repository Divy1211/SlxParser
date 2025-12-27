from sld import SldFile

from utils import timed

def main():
    with timed("read"):
        sld = SldFile.from_file("./files/b_indi_university_age3_x2.sld")
    print(f"{sld.frames[0].header.frame_type:b}")
    print(f"{sld.frames[0].damage_mask_layer.header.num_bytes = }")
    # print(f"{sld.frames[0].damage_mask_layer.header.offset_x1 = }")
    # print(f"{sld.frames[0].damage_mask_layer.header.offset_y1 = }")
    print(f"{len(sld.frames[0].damage_mask_layer.draw_commands) = }")

    total = 0
    for cmd in sld.frames[0].damage_mask_layer.draw_commands:
        total += cmd.draw_block_count

    print(f"{total = }")

    print(f"{len(sld.frames[0].damage_mask_layer.pixels) = }")
    print(f"{len(sld.frames[0].damage_mask_layer._null) = }")

    with timed("read"):
        sld = SldFile.from_file("./files/u_vil_male_villager_attackA_x2.sld")
    print(f"{sld.frames[0].header.frame_type:b}")

    print(f"{sld.frames[0].player_color_mask_layer.header.num_bytes = }")
    # print(f"{sld.frames[0].player_color_mask_layer.header.offset_x1 = }")
    # print(f"{sld.frames[0].player_color_mask_layer.header.offset_y1 = }")
    print(f"{len(sld.frames[0].player_color_mask_layer.draw_commands) = }")

    total = 0
    for cmd in sld.frames[0].player_color_mask_layer.draw_commands:
        total += cmd.draw_block_count

    print(f"{total = }")

    print(f"{len(sld.frames[0].player_color_mask_layer.pixels) = }")
    print(f"{len(sld.frames[0].player_color_mask_layer._null) = }")


if __name__ == "__main__":
    main()
