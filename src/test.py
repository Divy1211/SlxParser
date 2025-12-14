from sections.smx_sections import SmxFile
from utils import timed


def main():
    with timed("read"):
        smx = SmxFile.from_file("./files/attack_60_x2.smx", strict = False)

    print(len(smx.frames))

if __name__ == "__main__":
    main()
