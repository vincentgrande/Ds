import os,sys,glob

files=glob.glob("arm9/*")+glob.glob("arm11/*")

for i in files:
	if ".txt" in i:
		continue
	dpath=i+".txt"
	if not os.path.exists(dpath):
		os.system("luma3ds_exception_dump_parser %s > %s" % (i,dpath))
		print(dpath)