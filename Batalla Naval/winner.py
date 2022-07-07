import os
import time
def ganador():
    espacios=" "
    for i in range(10):
        os.system("clear")

        print()
        print("{} HAS GANADO".format(espacios))
        print("{} \ O /  ".format(espacios))
        print("{}   |    ".format(espacios))
        print("{} /   \  ".format(espacios))

        espacios +=" "

        time.sleep(0.3)
        os.system("clear")

        print()
        print("{} HAS GANADO".format(espacios))
        print("{}  __O__   ".format(espacios))
        print("{}    |     ".format(espacios))
        print("{}  /   |   ".format(espacios))
        

        espacios +=" "
        time.sleep(0.3)
        os.system("clear")

        print()
        print("{} HAS GANADO".format(espacios))
        print("{}     O    ".format(espacios))
        print("{}  /  | \  ".format(espacios))
        print("{}   |  \   ".format(espacios))

        espacios +=" "
        time.sleep(0.3)
        os.system("clear")



    