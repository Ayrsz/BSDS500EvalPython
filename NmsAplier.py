import cv2 as cv
import os
import numpy as np
import scipy as sci
from pdi.mat2png import mat2png

dirPREDS = os.path.abspath("./sources/PREDS/MATLAB/")
targetPNGPREDS = os.path.abspath("./sources/PREDS/PNG/")
targetNMS = os.path.abspath("./sources/NMS/")

applyNMS = True

mat2png(dirPREDS, targetPNGPREDS)

