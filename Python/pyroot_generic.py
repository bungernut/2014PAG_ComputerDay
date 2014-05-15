import ROOT
ROOT.gROOT.SetStyle("Plain")
ROOT.gStyle.SetPalette(1)
ROOT.gStyle.SetOptStat(1111)
ROOT.gStyle.SetOptFit(1111)

h1 = ROOT.TH1I('h1','RandomWalk',40,-20,20)
h1.Sumw2()
num_sims = 1000
num_steps = 20
c1 = ROOT.TCanvas("c1","RandWalk",800,500)

for i in range(num_sims):
    x = 0
    for i in range(num_steps):
        #ROOT.rand() returns a random integer
        move_dir = ROOT.rand() % 2
        if move_dir == 0:
            x += -1
        if move_dir == 1:
            x += 1
    h1.Fill(x)

h1.SetLineColor(4)
h1.Draw()
gauss = ROOT.TF1("Gaussiann","[0]*exp(-1*x^2/[1])",-50,50);
res = h1.Fit("gaus", "W", "",0,0);
gauss.Draw("same")

#c1 = ROOT.gDirectory.Get("c1")
c1.Print("random_walk.png")

