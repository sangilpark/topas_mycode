import sys, os
from ROOT import *
import numpy as np

#gStyle.SetCanvasPreferGL(1)
dir_path = sys.argv[1]

fin = TFile(dir_path+'/result_Tree.root')
nkeys = fin.GetNkeys()
keys = fin.GetListOfKeys()
fout = TFile(dir_path+'/histograms_1D.root','recreate')

hist_1d = {}
for idx, key in enumerate(keys):
    tree = key.ReadObj()
    nentries = tree.GetEntries()
    histName = tree.GetName()
    print(idx, key, type(key), tree, type(tree), tree.GetName())
    hist_1d[histName] = TH1D(histName,histName,200,0,200)
    for i in range(nentries):
        tree.GetEntry(i)
        x = tree.x
        y = tree.y
        z = tree.z
        v = tree.value
        
        # apply cut if needed
        if TMath.IsNaN(v) : continue
        #if z > 80 : continue

        hist_1d[histName].SetBinContent(z+1,v)
        #hist_1d[histName].SetBinContent(x+1,v)
        print(v)
        
    hist_1d[histName].Write()

