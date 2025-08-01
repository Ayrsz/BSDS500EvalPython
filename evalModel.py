from pdi.nmsMex import *
from funcs.readPreds import *
from funcs.edgesEvalDir import *
import os
import scipy as sci
import cv2 as cv

gtDir = os.path.abspath("./sources/GT/test/")
targetDir = os.path.abspath("./sources/PREDS/PNG/")


apply_thin = True
apply_nms = True



ODS, OIS, AP = edgesEvalDir(resDir = targetDir, gtDir=gtDir, pDistr ="", thresholds=10, tolerance = 0.0075, thin = True)
