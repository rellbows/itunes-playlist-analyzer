"""
Filename: playlist.py
Description: Script that can parse and analyze iTunes playlist files. Covered in "Python Playground" book by Mahesh Venkitachalam.

TODO: 
1) Test out 'findDuplicates' method
2) Pick up on 'Extracting Duplicates'
"""

import pList

def findDuplicates(fileName):
	"""
	Find duplicate tracks in given playlist.
	"""
	print('Finding duplicate tracks in %s...' % fileName)
	# read in playlist
	pList = plist.lib.readPlist(fileName)
	# get the tracks
	tracks = plist['Tracks']
	# create a track name dict
	trackNames = {}
	# iterate through tracks
	for trackId, track in tracks.items():
		try:
			name = track['Name']
			duration = track['Total Time]
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
