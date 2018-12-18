# you have to use initdir() before using functions from the module
import sys, os, pickle

log_file = None

def initdir(dirname):
	'''
	initdir(dirname)
	send me a path to a folder with songs_list.txt
	and I`ll initialize all necessary arguments
	'''

	_folderOfSongs = open(dirname + r'\songs_list.txt', mode='r', encoding='utf-8')

	global songs_list
	songs_list = eval(_folderOfSongs.read().rstrip())					# Making list of songs from songs_list.txt

	phm_pickle = open(os.path.abspath(os.path.dirname(sys.argv[0])) + r'\songs\phm.pickle', mode='rb')
	phm_songs = pickle.load(phm_pickle)
	songs_list.extend(phm_songs)
	phm_pickle.close()

	global songs_amount
	songs_amount = len(songs_list)

	global new_users_songs
	new_users_songs = open(dirname + r'\new_users_songs.txt', mode='a', encoding='utf-8')

def look4song(command):				# Looking for songs with the name in command and added them to list founded_songs
	com_low = command.lower().rstrip()
	founded_songs = []
	for x in songs_list:
		for i in x['song_name']:
			if i.startswith(com_low):
				founded_songs.append(x)
				break
	return founded_songs