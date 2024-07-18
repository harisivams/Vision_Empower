import winsound
file_path = "welcome.mp3"
winsound.PlaySound(file_path, winsound.SND_FILENAME | winsound.SND_LOOP)