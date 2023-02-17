import os
from . import zenoconsole

home_dir = os.path.expanduser("~")
output_file_path = os.path.join(home_dir, "zeno.txt")

if __name__ == '__main__':
    with open(output_file_path, "a") as out_file:
        zeno = zenoconsole.ZenoConsole(buffer=out_file)
        zeno.start()