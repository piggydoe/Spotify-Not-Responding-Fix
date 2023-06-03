import psutil

PROCNAME = "Spotify.exe"

for proc in psutil.process_iter():
    if proc.name() == PROCNAME:
        proc.kill()