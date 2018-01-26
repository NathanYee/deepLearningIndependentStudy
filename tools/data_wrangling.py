import os
from glob import glob
import pandas as pd

def folders_to_csv(train_path, label_path):
    """
    Transforms standard folder style training data into a csv structure for use in the
    fasti library. Does not run if the label csv already exists.
    
    :param train_path: the path of the training directory
    :type  train_path: string
    :param label_path: the path of labels.csv
    :type  label_path: string
    :returns: None
    """
    # exit if the label csv exists
    if os.path.exists(label_path):
        print("label.csv already exists - exiting")
        return
    
    # need to return to starting directory at the end
    CWD = os.getcwd()
    
    # 
    os.chdir(train_path)
    df = pd.DataFrame(columns=["file", "species"])
    for dir_ in os.listdir():
        os.chdir(dir_)
        dir_underscore = dir_.replace(' ', '_')
        for img in glob('*.png'):
            os.rename(img, '../'+img)
            df = df.append({"file": img, "species": dir_underscore}, ignore_index=True)
        os.chdir(os.path.join(CWD, train_path))
        os.rmdir(dir_)
    os.chdir(CWD)
    
    # return to starting directory
    df.to_csv(label_path, index=False)
    print("successfully created labels.csv")