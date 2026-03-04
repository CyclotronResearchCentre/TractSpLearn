#python 4_Register_track.py working_directory

from glob import glob
import numpy as np
from subprocess import call
import sys

# rep = sys.argv[-1]
rep ="/mnt/data/TractSPlearn/Data"
file_name = glob(rep+"/*/TOM_trackings/")
print(file_name)

for name in file_name:
    
    tmp = name.split("/")[-3]
    track_file = glob(name+"*tck")
    for track in track_file:
        track_tmp = track.split("/")[-1]
        cmd = "tcktransform -force "+track+" warped_template/"+tmp+"_warpfull2deformation_invert.mif.gz transformed_template/"+tmp+"_"+track_tmp
        print(cmd)
        call(cmd.split(" "))
