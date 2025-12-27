from smx import SmxFile

from utils import timed

def main():
    with timed("read"):
        smx = SmxFile.from_file("./files/b_west_blacksmith_age2_x1.smx")
    with timed("read"):
        smx = SmxFile.from_file("./files/u_bigboytank_x1.smx")
    with timed("read"):
        smx = SmxFile.from_file("./files/attack_60_x2.smx")

if __name__ == "__main__":
    main()
