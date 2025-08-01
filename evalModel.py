from pdi.nmsMex import *
from funcs.readPreds import *
from funcs.edgesEvalDir import *
import cv2 as cv
import os
import scipy as sci

dirGT = os.path.abspath("./sources/GT/test/")
dirPREDS = os.path.abspath("./sources/PREDS/MATLAB/")
targetNMS = os.path.abspath("./sources/NMS/")
targetDOC = ""

apply_thin = True
apply_nms = True

ODS, OIS, AP = edgesEvalDir(dirPREDS, dirGT, "", 10, 0.0075, True)
