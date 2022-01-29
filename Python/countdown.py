from time import sleep
name = 'Vikrant'
pi = 3.141592
print ('My name is %10s' %name)
print ('Value of pi = %1.4f' %pi)

hexnum = input ('Enter a hex number: ')
if hexnum[0:2] == '0x' or hexnum[0:2] == '0X':
    hexnum = (hexnum[2:])
else:
    hexnum = (hexnum)

print ('Number you entered in decimal is {} '.format(int(hexnum,16)))
i = 0

for i in range (30, 0, -1):
        #print ('Countdown: {} seconds' . format(i), end = '\r')
        print ('Countdown: %3d  seconds' %i, end = '\r')
        sleep (0.2)

print()

