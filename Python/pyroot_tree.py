import ROOT
ROOT.gROOT.SetStyle("Plain")
ROOT.gStyle.SetPalette(1)

mychain = ROOT.TChain("ntuple")
myhist = ROOT.TH1D("hist","hist Name",100,0,1)
myfit = ROOT.TF1("fitf","gaus")
c1 = ROOT.TCanvas()

dataCuts = "Zfit > 0 && Zfit < 7 && MinBin0 > 650 && MinBin0 < 700 "
dataCuts+= "&& MinBin1 > 650 && MinBin1 < 700 && abs(MinBin0 - MinBin1) < 10 "
dataCuts+= "&& EventCutID == 1 && Fprompt > 0 && HLatePE0 > 0 && HLatePE1 > 0"

mychain.Add("data/deap_ntp_013079_*.root")
print "Loaded %d entries"%mychain.GetEntries()
moar_cut = " && TotalPE > 120 && TotalPE < 240"
mychain.Draw("Fprompt>>hist", dataCuts + " && TotalPE > 120 && TotalPE < 240")

myhist.Fit("fitf","LL","",0.68,1)
c1.SetLogy(1)
