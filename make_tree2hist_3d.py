import sys, os
from ROOT import *
import numpy as np

gStyle.SetCanvasPreferGL(1)
dir_path = sys.argv[1]

fin = TFile(dir_path+'/result.root')
nkeys = fin.GetNkeys()
keys = fin.GetListOfKeys()
fout = TFile(dir_path+'/histograms.root','recreate')

hist_3d = {}
for idx, key in enumerate(keys):
    tree = key.ReadObj()
    nentries = tree.GetEntries()
    print(idx, key, type(key), tree, type(tree), tree.GetName())
    histName = tree.GetName()
    hist_3d[histName] = TH3D(histName,histName+';x;y;z',50,0,50,50,0,50,24,0,24)
    for i in range(nentries):
        tree.GetEntry(i)
        x = tree.x
        y = tree.y
        z = tree.z
        v = tree.value
        hist_3d[histName].Fill(x,y,z,v)
    hist_3d[histName].Write()

