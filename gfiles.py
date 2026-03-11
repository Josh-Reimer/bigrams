import os
rootdir = "gutenberg-dammit-files-v002/gutenberg-dammit-files/"
print(os.listdir("gutenberg-dammit-files-v002/gutenberg-dammit-files"))

for dir in os.listdir("gutenberg-dammit-files-v002/gutenberg-dammit-files"):
    for file in os.listdir(rootdir+dir):
        print(open(rootdir+dir+"/"+file).read())