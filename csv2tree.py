import os, sys
from ROOT import *

f = TFile("EDep.root","recreate")
tree = TTree('tree','data from csv')
nlines = tree.ReadFile('results_synthetic_lung/EDep.csv','x/I:y/I:z/I:value/D')
print(nlines)

tree.Write()
