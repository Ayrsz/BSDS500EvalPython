import os
#%   .pDistr     - [{'type','parfor'}] parameters for fevalDistr #?

def edgesEvalDir(resDir : os.path, gtDir : os.path, pDistr, thresholds : int, tolerance : float, thin : bool) -> (float, float, float): #ODS, OIS, AP

    assert os.path.exists(gtDir), f"Directory {gtDir} do not exists " 
    assert os.path.exists(resDir), f"Directory {resDir} do not exists "
    
    #Files names
    filesGT = os.listdir(gtDir)
    filesGT = sorted(filesGT)
    filesPRED = os.listdir(resDir)
    filesPRED = sorted(filesGT)
    assert len(filesGT) == len(filesPRED), f"Amount of files is diferent beetwen pred and gt {len(filesPRED)} | {len(filesGT)}"
    
    #Results var
    metrics = None
    #len of images
    n = len(filesGT)
    
    #Apply thinning

    #Run evaluation
    for i in range(n):
        #Name of the file
        name = filesGT[i].split(".")[0]
        assert filesGT[i].split(".")[1] == "mat", f"A non matlab {filesGT[i]} file"
        assert (name + ".png") in filesPRED, f"Cannot find {filesGT[i]} in png format "





if __name__ == "__main__":
    pass
