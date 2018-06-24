"""
This script records some known values of the first data point of the first
sweep from each channel of ABFs in the demo data folder.

It then uses pyABF to compare the first value to the known first value.
If the ABF reading class gets broken somehow and starts returning bad values,
this script will let you know about it.
"""
# import the pyabf module from this development folder
import os
import sys
PATH_HERE = os.path.abspath(os.path.dirname(__file__))
PATH_SRC = os.path.abspath(PATH_HERE+"/../src/")
PATH_DATA = os.path.abspath(PATH_HERE+"/../data/abfs/")
sys.path.insert(0, PATH_SRC)  # for importing
sys.path.append("../src/")  # for your IDE
import pyabf
import glob

FIRSTVALUES = {}
FIRSTVALUES['05210017_vc_abf1'] = ['-146.34189', '624.13208']
FIRSTVALUES['14o08011_ic_pair'] = ['-65.52124', '-56.12183']
FIRSTVALUES['14o16001_vc_pair_step'] = ['-25.87890', '-31.49414']
FIRSTVALUES['16d05007_vc_tags'] = ['0.85449']
FIRSTVALUES['16d22006_kim_gapfree'] = ['0.01007', '0.13641']
FIRSTVALUES['171116sh_0011'] = ['-125.73241']
FIRSTVALUES['171116sh_0012'] = ['-120.23925']
FIRSTVALUES['171116sh_0013'] = ['-103.51562']
FIRSTVALUES['171116sh_0014'] = ['-109.98534']
FIRSTVALUES['171116sh_0015'] = ['-119.38476']
FIRSTVALUES['171116sh_0016'] = ['-61.43188']
FIRSTVALUES['171116sh_0017'] = ['-61.70654']
FIRSTVALUES['171116sh_0018'] = ['-62.46948']
FIRSTVALUES['171116sh_0019'] = ['-62.43896']
FIRSTVALUES['171116sh_0020'] = ['72.75390']
FIRSTVALUES['171117_HFMixFRET'] = ['-0.43945', '-1897.58301', '0.06989', '0.07080']
FIRSTVALUES['17o05024_vc_steps'] = ['-21.36230']
FIRSTVALUES['17o05026_vc_stim'] = ['-16.11328']
FIRSTVALUES['17o05027_ic_ramp'] = ['-48.00415']
FIRSTVALUES['17o05028_ic_steps'] = ['-47.08862']
FIRSTVALUES['180415_aaron_temp'] = ['-0.35187', '17148.52344']
FIRSTVALUES['2018_04_13_0016a_original'] = ['-115.96679', '-15.25879']
FIRSTVALUES['2018_04_13_0016b_modified'] = ['353.90253', '22.71727']
FIRSTVALUES['model_vc_ramp'] = ['-138.42772']
FIRSTVALUES['model_vc_step'] = ['-140.13670']

def go():
    valuesNeedUpdating = False
    for fname in glob.glob(PATH_DATA+"/*.abf"):
        abf = pyabf.ABF(fname)
        firstValues = []  # one per channel
        for channel in abf.channelList:
            abf.setSweep(0, channel)
            firstValues.append("%.05f" % (abf.sweepY[0]))
        if abf.abfID in FIRSTVALUES.keys():
            assert firstValues == FIRSTVALUES[abf.abfID]
            print("Verified first values of", abf.abfID)
        else:
            valuesNeedUpdating = True
            print("FIRSTVALUES['%s'] = %s" % (abf.abfID, firstValues))
    if valuesNeedUpdating:
        print("PLEASE UPDATE FIRSTVALUES TO INCLUDE NEW DATA!")


if __name__ == "__main__":
    go()
    print("DONE")