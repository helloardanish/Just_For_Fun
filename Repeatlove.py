import itertools
import time

count=1
lst=['I', 'Love', 'You', 'A R']
#name='A R'
for i in itertools.cycle(lst):
    if count==200:
        break
    print(i,end=' ')
    time.sleep(0.1)
    if count%16==0:
        #print('A R', end=' ')
        print()
    
    count+=1
    