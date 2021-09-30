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
legend = TLegend(0.5,0.5,0.9,0.9)

hists = [
        #'EnergyDeposit',
        'DoseToWater',
        #'ProtonLET',
        'McNamara_RBE',
        'Carabe_RBE',
        'Wilkens_RBE',
        'Wedenberg_RBE',
        'Chen_RBE',
        'MKM_Kase_RBE',
        'MKM_PIDE_RBE',
        'MKMLET_RBE',
        'RMF_RBE',
        ]

for idx, hist in enumerate(hists):
    h = fin.Get(hist) 
    histName = h.GetName()
    if idx==0 :
        hist_tmp = h.Clone('')
        hist_tmp.SetTitle('')
        hist_tmp.GetYaxis().SetTitle('RBE(4 Gy)')
        hist_tmp.GetYaxis().SetRangeUser(0,2.5)
        hist_tmp.GetXaxis().SetTitle('depth(mm)')
        hist_tmp.Draw()
    
    if histName == 'DoseToWater' :
    #if histName == 'EnergyDeposit' :
        h.Scale(60/h.Integral())

    h.SetLineColor(idx+1)
    legend.AddEntry(h,histName,'l')
    h.Draw('hist same')

#for idx,key in enumerate(keys):
#    hist = key.ReadObj()
#    histName = hist.GetName()
#    if 'DoseToWater' in histName : 
#        hist.Scale(0.5/hist.Integral())
#
#    #if not 'RBE' in histName : continue
#    print(hist,histName)
#    if idx==0 :
#        hist_tmp = hist.Clone('')
#        hist_tmp.SetTitle('')
#        hist_tmp.GetYaxis().SetTitle('RBE(4 Gy)')
#        hist_tmp.GetYaxis().SetRangeUser(0.8,2)
#        hist_tmp.GetXaxis().SetTitle('depth(mm)')
#        hist_tmp.Draw()
#    else :
#        hist.SetLineColor(idx+1)
#        legend.AddEntry(hist,histName,'l')
#        hist.Draw('same')

legend.Draw('same')
c.SaveAs(dir_path+'/RBE.png')
