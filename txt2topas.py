#!/usr/bin/env python

import os, sys
from glob import glob

def main():
    txts = glob("*.txt")
    #print(txts)
    for txt in txts:
        topas = txt.replace("txt","topas")
        #print(topas)
        print('mv {} {}'.format(txt,topas))
        os.system('mv {} {}'.format(txt,topas))


if __name__=="__main__":
    main()
