import sys, os
from ROOT import *
import numpy as np

gStyle.SetCanvasPreferGL(1)
dir_path = sys.argv[1]

fin = TFile(dir_path+'/result_Tree.root')
nkeys = fin.GetNkeys()
keys = fin.GetListOfKeys()
fout = TFile(dir_path+'/histograms_3D.root','recreate')

hist_3d = {}
for idx, key in enumerate(keys):
    tree = key.ReadObj()
    nentries = tree.GetEntries()
    print(idx, key, type(key), tree, type(tree), tree.GetName())
    histName = tree.GetName()
    #hist_3d[histName] = TH3D(histName,histName+';x;y;z',50,0,50,50,0,50,50,0,50)
    hist_3d[histName] = TH3D(histName,histName+';x;y;z',1,0,1,1,0,1,200,0,200)
    for i in range(nentries):
        tree.GetEntry(i)
        x = tree.x
        y = tree.y
        z = tree.z
        v = tree.value
        # Apply cut if needed
        #if x<30 and y>20 and y<30 and z>20 and z<30 : 
        hist_3d[histName].Fill(x,y,z,v)
    hist_3d[histName].Write()

