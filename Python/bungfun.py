def get_run_tree_object(run):
    """
    Returns the tree object of the run specified. This uses the data catalogue
    to get the location of this run and then does all the shit I dont remember
    to return the thing I want, a friggin ROOT tree.
    """
    import ROOT
    ROOT.gSystem.Load("libEXOUtilities")
    if type(run) == type('a'): run = int(run)
    data_tree = ROOT.TChain("tree")
    print "Getting Run %d from datacat"%run
    run_info = ROOT.EXORunInfoManager.GetRunInfo(int(run),"Data/Processed/masked")
    for afile in run_info.GetRunFiles():
        print "Adding run_file",afile.GetFileLocation()
        data_tree.Add(afile.GetFileLocation())
    ne = data_tree.GetEntries()
    print "Run=%d, NumEvents=%d"%(run,ne)
    return data_tree


def get_event_data_masked(run, event):
    """Returns ed for event from masked files"""
    import ROOT
    ROOT.gSystem.Load("libEXOUtilities")
    run_info = ROOT.EXORunInfoManager.GetRunInfo(int(run),"Data/Processed/masked")
    data_tree = ROOT.TChain("tree")
    for afile in run_info.GetRunFiles():
        print "Adding run_file",afile.GetFileLocation()
        data_tree.Add(afile.GetFileLocation())
    ne = data_tree.GetEntries()
    print "Run=%d, NumEvents=%d"%(run,ne)
    data_tree.BuildIndex("fRunNumber","fEventNumber")
    data_tree.GetEntryWithIndex(run,event)
    return data_tree.EventBranch


def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
               j = cycles[i]
               indices[i], indices[-j] = indices[-j], indices[i]
               yield tuple(pool[i] for i in indices[:r])
               break
        else:
            return

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def get_pltXY_TH1D(hist):
    import numpy
    nbins = hist.GetNbinsX()
    x,y = [],[]
    for i in range(nbins):
        x.append(hist.GetBinCenter(i))
        y.append(hist.GetBinContent(i))
    return numpy.array(x),numpy.array(y)