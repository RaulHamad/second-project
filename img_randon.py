import os
import random
# Open a file

def list_champ():

    dirs = os.listdir("./static/img")

    # This would print all the files and directories
    print(type(dirs))
    a = random.randint(0, len(dirs))
    return(str(dirs[a]))  

