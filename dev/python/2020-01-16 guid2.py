"""
Invent a better (truly unique) GUID system
"""

import glob
import os
import sys
import matplotlib.pyplot as plt
import uuid
import datetime
import time
import hashlib

try:
    PATH_HERE = os.path.abspath(os.path.dirname(__file__))
    PATH_DATA = os.path.abspath(PATH_HERE+"../../../data/abfs/")
    PATH_SRC = os.path.abspath(PATH_HERE+"../../../src/")
    DATA_FOLDER = os.path.join(PATH_SRC, "../data/abfs/")
    sys.path.insert(0, PATH_SRC)
    import pyabf
except:
    raise EnvironmentError()


def countDuplicateGuids(useNewGuid=False):
    guids = []
    guidAndIDs = []
    for abfFilePath in glob.glob(DATA_FOLDER + "/*.abf"):
        abf = pyabf.ABF(abfFilePath)
        guid = abf.fileUUID if useNewGuid else abf.fileGUID
        guidAndIDs.append([guid, abf.abfID])
        guids.append(guid)

    duplicates = 0
    for guid, abfID in sorted(guidAndIDs):
        if guids.count(guid) > 1:
            print(f"{guid} DUPLICATE! {abfID}.abf")
            duplicates += 1
        else:
            print(f"{guid}  (unique)  {abfID}.abf")

    print(f"Found {duplicates} duplicates out of {len(guidAndIDs)} ABFs")


if __name__ == "__main__":
    #countDuplicateGuids(True)

    abf = pyabf.ABF(PATH_DATA+"/2019_07_24_0055_fsi.abf")
    print(abf.fileGUID)
    print(abf.fileUUID)
    print(abf.md5)
