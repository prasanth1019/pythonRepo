import os

i = 256*256
print('The value of i is %s' %i)

for arg in range(0, 250, 100):
    print('The value of arg is %s' %arg)


b = 1
a = 0
for arg in range(0, 10):
    temp = a + b
    a = b
    b = temp;
    print("Fibonacci series...%s" %temp)


userName = 'AravinthRamanathan'
lett = 'str'.strip()+'iii'
print(lett)

print(userName[0])
print(userName[0:8])


print(userName[:4])
print(userName[4:])

print("Negative indexes...%s" %userName[-2])
print("Negative indexes...%s" %userName[-10])

sampleChar =  "supercalifragilisticexpialidocious";
print(len(sampleChar))

#================================================

z = input('really quit???')
if z in ('Y', 'y'):
    print("Thanks a lot bro!!!")
else:
    print("No Thanks !!!")
#================================================
    def make_incrementor (n): return lambda x: x + n
    make_incrementor(3)

#=======================*******======================
os.stat('C:/Users/PRaman357/Desktop/pythonFirstProg.py')
print(os.stat('C:/Users/PRaman357/Desktop/pythonFirstProg.py').CONST_VALUE)











