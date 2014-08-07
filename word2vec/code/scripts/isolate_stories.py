from subprocess import call
import os
import re
import sys

# wget --continue --tries=20 --user=elissawolf --password='I7VwnhXeU' http://icwsm.cs.umbc.edu/data/icwsm2009/BLOGS-tiergroup-1.tar.gz

urls = ["http://icwsm.cs.umbc.edu/data/icwsm2009/BLOGS-tiergroup-1.tar.gz",
	"http://icwsm.cs.umbc.edu/data/icwsm2009/BLOGS-tiergroup-2.tar.gz",
	"http://icwsm.cs.umbc.edu/data/icwsm2009/BLOGS-tiergroup-3.tar.gz",
	"http://icwsm.cs.umbc.edu/data/icwsm2009/BLOGS-tiergroup-4.tar.gz",
	"http://icwsm.cs.umbc.edu/data/icwsm2009/BLOGS-tiergroup-5.tar.gz",
	"http://icwsm.cs.umbc.edu/data/icwsm2009/BLOGS-tiergroup-6.tar.gz",
	"http://icwsm.cs.umbc.edu/data/icwsm2009/BLOGS-tiergroup-7.tar.gz",
	"http://icwsm.cs.umbc.edu/data/icwsm2009/BLOGS-tiergroup-8.tar.gz",
	"http://icwsm.cs.umbc.edu/data/icwsm2009/BLOGS-tiergroup-9.tar.gz",
	"http://icwsm.cs.umbc.edu/data/icwsm2009/BLOGS-tiergroup-10.tar.gz",
	"http://icwsm.cs.umbc.edu/data/icwsm2009/BLOGS-tiergroup-11.tar.gz",
	"http://icwsm.cs.umbc.edu/data/icwsm2009/BLOGS-tiergroup-12.tar.gz",
	"http://icwsm.cs.umbc.edu/data/icwsm2009/BLOGS-tiergroup-13.tar.gz",
	"http://icwsm.cs.umbc.edu/data/icwsm2009/BLOGS-tiergroup-none.tar.gz"]

# Get and unpack all of the data
for i in range(3, 4):# len(urls)):
	dir = os.path.basename(urls[i])
	if os.path.exists(dir) == False:
		os.system("wget --continue --tries=20 --user=elissawolf --password='I7VwnhXeU' " + urls[i]) 
		os.system("tar -zxvf " + dir)

print("All data acquired.")

# This file tells us what lines to keep
file = '../icwsm09stories.txt'
#f = open(file, 'r')
#lines = f.readlines()
#lines = [line.split() for line in lines]

# Keep all lines from personal stories here
personal_stories = []
# So we don't read through any one data file more than once
data_files = {}

with open(file, 'r') as f:
	for item in f:
		item = item.split()
		# line[1] > 0 if this item is a personal story
		if (item[1] > 0):
			path = item[0]
			if path in data_files:
				data_file = data_files[path]
			else:
				try:
					with open(path, 'r') as data_file:
						data_file = data_file.readlines()
						data_files[path] = data_file
						print 'Successfully opened: ' + path
				except IOError:
					# print 'could not open file: ' + path
					continue

			#try:
			#	with open(path, 'r') as data_file:
			#		lines = data_file.readlines()
			#except IOError:
			#	continue

			# take all lines for this story
			for i in range(int(item[2]), int(item[3])+1):
				line = data_file[i]
				line = re.sub('<.*?>', '', line.strip())
				if line != '':
					for word in line.split():
						personal_stories.append(word)
		print("."),

with open('out.txt', 'w') as out:
	for item in personal_stories:
		out.write("%s, " % item)
				

