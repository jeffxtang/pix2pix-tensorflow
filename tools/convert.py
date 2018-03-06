import os

file_names = os.listdir("photos/resized/")
for f in file_names:
    if f.find(".png") != -1:
    	os.system("convert photos/resized/" + f + " -blur 0x3 photos/blurry/" + f)
    	print("photos/resized/" + f)

file_names = os.listdir("photos/resized/val/")
for f in file_names:
    if f.find(".png") != -1:
        os.system("convert photos/resized/" + f + " -blur 0x3 photos/blurry/" + f)
        print("photos/resized/" + f)
