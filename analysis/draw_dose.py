import sys, os
from ROOT import *

gStyle.SetOptStat(False)

f_rbe = TFile('results_SOBP_100MeV_Width0.6/histograms_1D.root')
f_patient = TFile('results_RandoPhantom_SOBP_100MeV_Width0.6/histograms_1D.root')

h_rbe_McNamara = f_rbe.Get('McNamara_RBE')
h_patientdose = f_patient.Get('DoseToMedium')

h_patientdose_ConstantRBE = h_patientdose.Clone()
h_patientdose_ConstantRBE.Scale(1.1)

h_patientdose_McNamaraRBE = h_patientdose.Clone()

nbins = h_rbe_McNamara.GetNbinsX()
print(nbins)

for i in range(1,80):
    print(i, h_patientdose.GetBinContent(i), h_rbe_McNamara.GetBinContent(i+20))
    h_patientdose_McNamaraRBE.SetBinContent(i,h_patientdose.GetBinContent(i)*h_rbe_McNamara.GetBinContent(i+20))

legend = TLegend(0.5,0.6,0.8,0.8)
legend.AddEntry(h_patientdose,'Dose','l')
legend.AddEntry(h_patientdose_ConstantRBE,'Dose*1.1','l')
legend.AddEntry(h_patientdose_McNamaraRBE,'Dose*McNamaraRBE','l')

h_patientdose.SetLineColor(kBlack)
h_patientdose_ConstantRBE.SetLineColor(kBlue)
h_patientdose_McNamaraRBE.SetLineColor(kRed)

c = TCanvas('c','',1500,1500)
h_patientdose_McNamaraRBE.Draw('hist')
h_patientdose.Draw('hist same')
h_patientdose_ConstantRBE.Draw('hist same')
legend.Draw()

c.SaveAs('PatientDose_rbe.png')
