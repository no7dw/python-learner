import os, shutil
print os.listdir("..")
shutil.copytree("../stand","../stand2")
shutil.rmtree("../stand2")
