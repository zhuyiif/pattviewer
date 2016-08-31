
import numpy as np

import scipy.misc as smp

pattdata = np.loadtxt('kanji.patt', skiprows=0, unpack=True)

rows = len(pattdata)
columes    = len(pattdata[0])
data = np.zeros( (columes,rows,3), dtype=np.uint8 )

listIndex = 0;
for list in pattdata:
    count = 0

    for x in list:

        item = int(x)
        if (item > 125):
            item = [255,255,255]
        else:
            item = [0,0,0]

        data[count,listIndex] = item
        print(str(count) + ' ' + str(listIndex))
        count+=1
    listIndex += 1;

img = smp.toimage( data )       # Create a PIL image
img.show()