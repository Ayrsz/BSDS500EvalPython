import cv2 as cv
import scipy as sci
import numpy as np
import os

def mat2png(dirMatlabPred, dirPNGPRED):

    if os.listdir(dirMatlabPred) <= os.listdir(dirPNGPRED):
        print("| !!DirMatlab and DirPNG of the same size, will not convert matlab to png!! |")
        return 

    print("| Converting MATLAB preds to PNG |")
    filesMAT = os.listdir(dirMatlabPred)    
    
    for file in filesMAT:
        name = file.split(".")[0]
        assert file.split(".")[1] == "mat", f"Pred with no matlab file {file}"
        fileMat = os.path.join(dirMatlabPred, file)
        im = sci.io.loadmat(fileMat)
        im = im["image_data"] # Could be changed, depende on how the images was saved

        newFile = os.path.join(dirPNGPRED, name + ".png")
        print(newFile)
        cv.imwrite(newFile, im)