import os,sys
from ROOT import *

f = TFile("output_mybox.root","READ")

tree = f.Get("PhaseSpaceScore")

h_EDep = f.Get("EDep")



nev = tree.GetEntries()

print nev
#for iev in range(nev):
#    tree.GetEntry(iev)
#    print "Position X Y Z [cm] : ", tree.Position_X__cm_, tree.Position_Y__cm_, tree.Position_Z__cm_

c = TCanvas("canvas","",800,600)
h_EDep.Draw("COLZ")
c.SaveAs("EDep.png")
