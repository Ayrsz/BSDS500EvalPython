import os

#%   .pDistr     - [{'type','parfor'}] parameters for fevalDistr #?

def edgesEvalDir(resDir : os.path, gtDir : os.path, pDistr, thresholds : int, tolerance : float, thin : bool) -> (float, float, float): #ODS, OIS, AP
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", os.getcwd())

    assert os.path.exists(gtDir), f"Directory {gtDir} do not exists " 
    assert os.path.exists(resDir), f"Directory {resDir} do not exists "
    
    #Files names
    filesGT = os.listdir(gtDir)
    filesGT = sorted(filesGT)
    filesPRED = os.listdir(resDir)
    filesPRED = sorted(filesGT)
    
    #Results var
    metrics = None

    #len of images
    n = len(filesGT)


    for i in range(n):
        #Name of the file
        name = filesGT[i].sep(".")[0]
        
        #garant gt as a .mat file
        assert filesGT[i].sep(".")[1] == ".mat", f"A non matlab {filesGT[i]} file"
        assert filesPRED.find(name + ".png"), f"Cannot find {filesGT[i]} in png format "





if __name__ == "__main__":
    pass
