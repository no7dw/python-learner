import os, shutil
print os.listdir ("./")
for file in os.listdir("."):
	if os.path.splitext(file)[1]==".txt" and not os.path.isdir("./bak"):
		os.mkdir("./bak")
		print file
		#shutil.copy(file, os.path.join("back", file))
