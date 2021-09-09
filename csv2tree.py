import os, sys
from ROOT import *
import glob

dir_path = sys.argv[1]
csv_files = glob.glob(dir_path+'/*.csv')
rootfile = TFile(dir_path + "/result.root","recreate")
tree = {}
for i, f in enumerate(csv_files):
    tree_name = f.split('/')[-1].replace('.csv','')
    tree[i] = TTree(tree_name,'tree from csv')
    tree[i].ReadFile(f,'x/I:y/I:z/I:value/D')
    tree[i].Write()
    print('Tree for '+tree_name)

print('Done')
