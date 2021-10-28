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
gPad.DrawFrame(0,0,160,2)
legend = TLegend(0.1,0.6,0.3,0.9)

h_EnergyDeposit = fin.Get('EnergyDeposit') 
h_ProtonLET = fin.Get('ProtonLET') 
h_Wedenberg_RBE = fin.Get('Wedenberg_RBE') 

h_tmp = h_EnergyDeposit.Clone('')
h_tmp.SetTitle('')
h_tmp.GetXaxis().SetTitle('depth(mm)')
h_tmp.GetXaxis().SetRangeUser(0,160)
h_tmp.GetXaxis().SetNdivisions(520)
h_tmp.GetYaxis().SetTitle('RBE')
h_tmp.GetYaxis().SetTitleColor(kRed)
h_tmp.GetYaxis().SetLabelColor(kRed)
h_tmp.GetYaxis().SetRangeUser(0,2.0)
h_tmp.GetYaxis().SetNdivisions(225)
h_tmp.Draw()

h_EnergyDeposit.Scale(200/h_EnergyDeposit.Integral())
h_EnergyDeposit.SetLineColor(kBlack)
h_EnergyDeposit.SetLineWidth(4)
h_EnergyDeposit.Smooth()
h_EnergyDeposit.Draw('C hist same')

h_EnergyDeposit_applyConstRBE = h_EnergyDeposit.Clone()
h_EnergyDeposit_applyConstRBE.Scale(1.1)
h_EnergyDeposit_applyConstRBE.SetLineColor(kGreen)
h_EnergyDeposit_applyConstRBE.SetLineWidth(4)
h_EnergyDeposit_applyConstRBE.Smooth()
h_EnergyDeposit_applyConstRBE.Draw('C hist same')

h_EnergyDeposit_applyModelRBE = h_EnergyDeposit.Clone()
h_EnergyDeposit_applyModelRBE.Multiply(h_Wedenberg_RBE)
h_EnergyDeposit_applyModelRBE.SetLineColor(kViolet)
h_EnergyDeposit_applyModelRBE.SetLineWidth(6)
h_EnergyDeposit_applyModelRBE.Smooth()
h_EnergyDeposit_applyModelRBE.Draw('C hist same')

h_ProtonLET.Scale(0.1)
h_ProtonLET.SetLineColor(kBlue)
h_ProtonLET.SetLineWidth(4)
h_ProtonLET.Smooth()
h_ProtonLET.Draw('C hist same')

h_Wedenberg_RBE.SetLineColor(kRed)
h_Wedenberg_RBE.SetLineWidth(6)
h_Wedenberg_RBE.Smooth()
h_Wedenberg_RBE.Draw('C hist same')

legend.AddEntry(h_EnergyDeposit,'Dose','l')
legend.AddEntry(h_ProtonLET,'Proton LET','l')
legend.AddEntry(h_Wedenberg_RBE,'RBE (Wedenberg)','l')
legend.AddEntry(h_EnergyDeposit_applyConstRBE,'Dose * 1.1','l')
legend.AddEntry(h_EnergyDeposit_applyModelRBE,'Dose * RBE','l')

yaxis_right = TGaxis(160,0,160,2,0,20,525,'+L')
yaxis_right.SetTitle('LET (MeV/mm/(g/cm3))')
yaxis_right.SetTitleColor(kBlue)
yaxis_right.SetTitleSize(0.04)
yaxis_right.SetLineColor(kBlue)
yaxis_right.SetLabelColor(kBlue)
yaxis_right.SetLabelOffset(0.01)
yaxis_right.SetLabelSize(0.03)
#yaxis_right.SetTickSize(0.2)
yaxis_right.Draw()

c.SetGrid()
c.SetFillStyle(4000)
legend.Draw('same')
c.SaveAs(dir_path+'/Dose_LET_RBE.png')
