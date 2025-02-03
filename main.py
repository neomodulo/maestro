import time, pexpect
print("maestro cli - neomodulo 2025\n")

try:
    vlc = pexpect.spawn("vlc -I rc '../../test track.mp3'", encoding='utf-8')
except pexpect.exceptions.ExceptionPexpect:
    print("Error: Could not find VLC. Is it in your PATH?\n")
    print("Windows:   Add path to VLC in Control Panel")
    print("macOS:     Add path to VLC to /etc/paths ")
    quit()

for i in range(1,3):
    time.sleep(2)
    vlc.expect('> ')
    print("pause",i)
    vlc.sendline('pause')

time.sleep(2)
vlc.kill(1)
print('is alive:', vlc.isalive())
