from sld import SldFile

from utils import timed

def main():
    with timed("read"):
        sld = SldFile.from_file("./files/b_indi_university_age3_x2.sld")
    with timed("read"):
        sld = SldFile.from_file("./files/u_vil_male_villager_attackA_x2.sld")

if __name__ == "__main__":
    main()
