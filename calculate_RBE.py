import os, sys
from ROOT import *
from ROOT import TMath
import numpy as np


### V79 CellLine ###
AlphaBetaRatiox = 1.412


if len(sys.argv) < 2:
    print("Error: please put dir_path as argument 1")
    exit(0)

dir_path = sys.argv[1]
f = TFile(dir_path+'/histograms.root')
hProtonLET = f.Get('ProtonLET')
hDoseToMedium = f.Get('DoseToMedium')

nbinsx = hProtonLET.GetNbinsX()
nbinsy = hProtonLET.GetNbinsY()
nbinsz = hProtonLET.GetNbinsZ()

hProtonRBE_Wedenberg = TH3D('ProtonRBE_Wedenberg','ProtonRBE_Wedenberg',nbinsx,0,nbinsx,nbinsy,0,nbinsy,nbinsz,0,nbinsz)
hProtonRBE_MinMax = TH3D('ProtonRBE_MinMax','ProtonRBE_MinMax',nbinsx,0,nbinsx,nbinsy,0,nbinsy,nbinsz,0,nbinsz)

for x in range(nbinsx):
    for y in range(nbinsy):
        for z in range(nbinsz):
            LET_d = hProtonLET.GetBinContent(x+1,y+1,z+1)
            Phys_dose = hDoseToMedium.GetBinContent(x+1,y+1,z+1)
            if not Phys_dose==0 :
                ## Wedenberg
                RBE_Wedenberg = 1/(2*Phys_dose) * (TMath.Sqrt(AlphaBetaRatiox*AlphaBetaRatiox + 4*Phys_dose*(AlphaBetaRatiox+ 0.434*LET_d) + 4*Phys_dose*Phys_dose) - AlphaBetaRatiox)

                ## RBE Min-Max : Carabe, McNamara etc..
                RBE_Max = 0.843 + 0.154*(2.686/AlphaBetaRatiox)*Phys_dose
                RBE_Min = 1.09 + 0.0006*(2.686/AlphaBetaRatiox)*Phys_dose
                RBE_MinMax = 1/(2*Phys_dose) * (TMath.Sqrt(AlphaBetaRatiox*AlphaBetaRatiox + 4*Phys_dose*AlphaBetaRatiox*RBE_Max + 4*RBE_Min*RBE_Min*Phys_dose*Phys_dose) - AlphaBetaRatiox)
            else : 
                RBE_Wedenberg = 1.0
                RBE_MinMax = 1.0
            
            hProtonRBE_Wedenberg.SetBinContent(x+1,y+1,z+1,RBE_Wedenberg)
            hProtonRBE_MinMax.SetBinContent(x+1,y+1,z+1,RBE_MinMax)
           
fout = TFile(dir_path+'/RBE.root','recreate')
hProtonRBE_Wedenberg.Write()
hProtonRBE_MinMax.Write()
