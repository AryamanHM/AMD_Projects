def ftale(x):
	command="perl hipify-perl "+os.path.basename(x)+" > "+os.path.basename(x)+".hip"
	os.system(command)
	

def fall(y):
	"""
	dir_list = os.listdir(y)
	for i in dir_list:
		if i.lower().endswith('.cu') or i.lower().endswith('.cpp'):
			command="perl hipify-perl "+i+" > "+i+".hip"
			os.system(command)
			"""
	pattern = ["*.cu","*.cpp"]
	for path, subdirs, files in os.walk(y):
		for name in files:
			if fnmatch(name, pattern):
				##print(os.path.join(path, name))
				f=os.path.join(path, name)
				command="perl hipify-perl "+f+" > "+f+".hip"
				os.system(command)
            

from fnmatch import fnmatch
import argparse
import os
parser=argparse.ArgumentParser()
parser.add_argument("-t", "--tale", help = "Hipify Single Sample")
parser.add_argument("-a", "--all", help = "Hipify all Samples")
args=parser.parse_args()
if args.tale:
	x=args.tale
	##print(x)
	ftale(x)
if args.all:
	y=args.all
	##print(y)
	fall(y)

	
