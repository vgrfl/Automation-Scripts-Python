import random, os, sys, subprocess

music_dir = '/home/vg/Music'  # Specify music directory path
songs = os.listdir(music_dir)

song = random.randint(0,len(songs))

print(songs[song])  

filename = os.path.join(music_dir, songs[0])

# Use file launching commands based on the OS
if sys.platform == "win32":
    os.startfile(filename)
else:
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, filename])