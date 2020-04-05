import json
import shutil
import os

#C:\Users\ryant\AppData\Roaming\.minecraft\assets\indexes\1.15.json
#C:\Users\ryant\AppData\Roaming\.minecraft\assets\objects\

f = open("C:\\Users\\ryant\\AppData\\Roaming\\.minecraft\\assets\\indexes\\1.15.json", "r")
cache_objects = json.loads(f.read())["objects"]
for x in cache_objects:
	if (x.startswith("minecraft/lang/")):
		objHash = cache_objects[x]["hash"]
		shutil.copyfile(os.path.join("C:\\Users\\ryant\\AppData\\Roaming\\.minecraft\\assets\\objects\\", objHash[:2], objHash), x.replace("minecraft/lang/", ""))