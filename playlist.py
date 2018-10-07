"""
Filename: playlist.py
Description: Script that can parse and analyze iTunes playlist files. Covered in "Python Playground" book by Mahesh Venkitachalam.

TODO: 
1) Test out 'findDuplicates' method
2) Pick up on 'Extracting Duplicates'
"""

import argparse
import plistlib

def findDuplicates(fileName):
	"""
	Find duplicate tracks in given playlist.
	"""
	print('Finding duplicate tracks in %s...' % fileName)
	# read in playlist
	plist = plistlib.readPlist(fileName)
	# get the tracks
	tracks = plist['Tracks']
	# create a track name dict
	trackNames = {}
	# iterate through tracks
	for trackId, track in tracks.items():
		try:
			name = track['Name']
			duration = track['Total Time']
			# checks if there is an entry matching
			if name in trackNames:
				# if name/duration match, inc count
				# round track length to nearest second
				if duration//1000 == trackNames[name][0]//1000:
					count = trackNames[names][1]
					trackNames[name] = (duration, count + 1)
				else:
					# add dictionary entry as tuple (duration, count)
					trackNames[name] = (duration, 1)
		except:
			# ignore
			pass
	# store duplicates as (name, count) tuples
	dups = []
	for k, v in trackNames.items():
		if v[1] > 1:
			dups.append((v[1], k))
	# save duplicates to a file
	if len(dups) > 0:
		print("Found %d duplicates. Track names saved to dup.txt" % len(dups))
	else:
		print("No duplicate tracks found!")
	f = open("dups.txt", "w")
	for val in dups:
		f.write("[%d] %s\n" % (val[0], val[1]))
	f.close()

def main():
	# create parser
	descStr = """
	This program analyzes playlist files (.xml) exported from iTunes.
	"""
	parser = argparse.ArgumentParser(description=descStr)
	# adds a mutually exclusive group of arguments
	group = parser.add_mutually_exclusive_group()

	# add expected arguments
	# group.add_argument('--common', nargs='*', dest='plFiles', required=False)
	# group.add_argument('--stats', dest='plFile', required=False)
	group.add_argument('--dup', dest='plFileD', required=False)

	# parse args
	args=parser.parse_args()

	# if args.plFiles:
		# find common tracks
		# findCommonTracks(args.plFiles)
	# elif args.p1Files:
		# plot stats(args.plFile)
		# plotStats(args.plFile)
	if args.plFileD:
		# find duplicate tracks
		findDuplicates(args.plFileD)
	else:
		print("Ooops, looks like the option you entered is not valid!")

# main method
if __name__ == '__main__':
	main()		
