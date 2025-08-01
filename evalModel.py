from pdi.nmsMex import *
from funcs.readPreds import *
from funcs.edgesEvalDir import *
import os
import scipy as sci
import cv2 as cv

gtDir = os.path.abspath("./sources/GT/test/")
dirPREDS = os.path.abspath("./sources/PREDS/MATLAB/")
targetPNGPREDS = os.path.abspath("./sources/PREDS/PNG/")
targetNMS = os.path.abspath("./sources/NMS/")
targetDOC = ""

apply_thin = True
apply_nms = True



ODS, OIS, AP = edgesEvalDir(dirPREDS, gtDir=gtDir, nmsDir = targetNMS, pDistr ="", thresholds=10, tolerance = 0.0075, thin = True, nms = True)
