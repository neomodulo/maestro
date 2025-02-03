import time, pexpect
print("maestro cli - neomodulo 2025\n")

vlc = pexpect.spawn("vlc -I rc '../../test track.mp3'", encoding='utf-8')

for i in range(1,3):
    time.sleep(2)
    vlc.expect('> ')
    print("pause",i)
    vlc.sendline('pause')

time.sleep(2)
vlc.kill(1)
print('is alive:', vlc.isalive())
