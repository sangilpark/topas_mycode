import sys, os
from ROOT import *

gStyle.SetOptStat(False)

dir_path = sys.argv[1]
fin = TFile(dir_path+'/histograms_1D.root')

nkeys = fin.GetNkeys()
keys = fin.GetListOfKeys()
#fout = TFile(dir_path+'/RBE_1D.root','recreate')

hist_1d = {}
c = TCanvas('canvas','canvas',1500,1500)
legend = TLegend(0.1,0.6,0.3,0.9)

hists = [
        'EnergyDeposit',
        #'DoseToWater',
        'Wedenberg_RBE',
        'Wilkens_RBE',
        #'Carabe_RBE',
        #'Chen_RBE',
        #'McNamara_RBE',
        #'MKM_Kase_RBE',
        #'MKM_PIDE_RBE',
        #'MKMLET_RBE',
        #'RMF_RBE',
        #'ProtonLET',
        ]

for idx, hist in enumerate(hists):
    h = fin.Get(hist) 
    histName = h.GetName()
    if idx==0 :
        hist_tmp = h.Clone('')
        hist_tmp.SetTitle('')
        hist_tmp.GetXaxis().SetTitle('depth(mm)')
        hist_tmp.GetXaxis().SetRangeUser(0,100)
        hist_tmp.GetXaxis().SetNdivisions(520)
        hist_tmp.GetYaxis().SetTitle('RBE(4 Gy)')
        hist_tmp.GetYaxis().SetRangeUser(0.8,2.0)
        hist_tmp.GetYaxis().SetNdivisions(225)
        hist_tmp.Draw()
    
    #if histName == 'DoseToWater' :
    if histName == 'EnergyDeposit' :
        h.Scale(150/h.Integral())

    h.SetLineColor(idx+1)
    h.SetLineWidth(2)
    h.Smooth()
    legend.AddEntry(h,histName,'l')
    h.Draw('C hist same')

c.SetGrid()
c.SetFillStyle(4000)
legend.Draw('same')
c.SaveAs(dir_path+'/RBE.png')
