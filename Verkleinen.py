from PIL import Image
import glob
import os

sizes = [["extra small", (25, 25)], ["small", (64, 64)],
         ["medium", (278, 278)], ["large", (558, 558)]]

for size in sizes:
    if not os.path.exists(os.getcwd() + "/" + size[0]):
        os.makedirs(os.getcwd() + "/" + size[0])

for infile in glob.glob("*.[jpg][pni][gf]"):
    file, ext = os.path.splitext(infile)
    for size in sizes:
        im = Image.open(infile)
        im.thumbnail(size[1])
        subdir = os.getcwd() + "/" + size[0] + "/"
        im.save(subdir + os.path.basename(file) + "_1.png", "PNG")
