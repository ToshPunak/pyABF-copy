"""
Test error messages when loading ABFs and ATFs with the wrong methods.
"""

import os
import sys
PATH_HERE = os.path.abspath(os.path.dirname(__file__))
PATH_DATA = os.path.abspath(PATH_HERE+"../../../data/abfs/")
PATH_SRC = os.path.abspath(PATH_HERE+"../../../src/")
sys.path.insert(0, PATH_SRC)

import pyabf

if __name__ == "__main__":
    abfFile = PATH_DATA + "/14o08011_ic_pair.abf"
    atfFile = PATH_DATA + "/model_vc_step.atf"

    # normal
    print(pyabf.ABF(abfFile))
    print(pyabf.ATF(atfFile))

    # errors
    #print(pyabf.ABF(atfFile))
    #print(pyabf.ATF(abfFile))

