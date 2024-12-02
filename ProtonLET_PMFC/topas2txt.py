#!/usr/bin/env python

import os, sys
from glob import glob

def main():
    dir = sys.argv[1]
    topases = glob(dir+"/*.topas")
    for topas in topases:
        txt = topas.replace("topas","txt")
        #print(topas)
        print('mv {} {}'.format(topas,txt))
        os.system('mv {} {}'.format(topas,txt))


if __name__=="__main__":
    main()
