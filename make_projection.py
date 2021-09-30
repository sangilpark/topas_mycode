import sys, os
from ROOT import *
import numpy as np

gStyle.SetOptStat(0)
#gStyle.SetCanvasPreferGL(1)

dir_path = sys.argv[1]

fin = TFile(dir_path+'/histograms_3D.root')
fout = TFile(dir_path+'/histograms_2D.root','recreate')

#fin = TFile(dir_path+'/RBE.root')
#fout = TFile(dir_path+'/RBE_2d_projection.root','recreate')

nkeys = fin.GetNkeys()
keys = fin.GetListOfKeys()

fout.cd()

for idx, key in enumerate(keys):
    h3 = key.ReadObj()
    histname = h3.GetName()
    print(histname)
    nxbins = h3.GetNbinsX()
    nybins = h3.GetNbinsY()
    nzbins = h3.GetNbinsZ()
    
    # x-y slice
    for zbin in range(nzbins):
        h3_xy = h3.Clone()
        h3_xy.GetZaxis().SetRange(zbin,zbin+1)
        h2_xy = h3_xy.Project3D('xy')
        h2_xy.SetOption('COLZ')
        h2_xy.Write()
        
    # x-z slice
    for ybin in range(nybins):
        h3_xz = h3.Clone()
        h3_xz.GetYaxis().SetRange(ybin,ybin+1)
        h2_xz = h3_xz.Project3D('xz')
        h2_xz.SetOption('COLZ')
        h2_xz.Write()
        
    # y-z slice
    for xbin in range(nxbins):
        h3_yz = h3.Clone()
        h3_yz.GetXaxis().SetRange(xbin,xbin+1)
        h2_yz = h3_yz.Project3D('yz')
        h2_yz.SetOption('COLZ')
        h2_yz.Write()
        
