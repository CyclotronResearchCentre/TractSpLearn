#python Register_AD.py working_directory
#Needs that AD map was named AD_MNI_nii.gz in each patient folder

from glob import glob
import numpy as np
from subprocess import call
import sys

# rep = sys.argv[-1]
# rep ="/home/jiqing/postdoc/brian_2024/TractLearn_with_Jinqing/data/Lund_Boxers_7T"
rep = "/mnt/data/TractSPlearn/Data"
file_name = glob(rep+ "/*/AD_MNI.nii.gz")
print(file_name)

for name in file_name:
    tmp = name.split("/")[-2]
    cmd = "mrtransform -force -template template_FOD.nii.gz -warp warped_template/"+tmp+"_warpfull2deformation.mif.gz "+name+" transformed_template/"+tmp+"_AD_template.nii.gz"
    print(cmd)
    call(cmd.split(" "))
