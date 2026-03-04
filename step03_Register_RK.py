#python Register_RK.py working_directory
#Needs that RK map was named RK_MNI_nii.gz in each patient folder

from glob import glob
import numpy as np
from subprocess import call
import sys

# rep = sys.argv[-1]
rep = "/mnt/data/TractSPlearn/Data"

file_name = glob(rep+ "/*/RK_MNI.nii.gz")
print(file_name)

for name in file_name:
	tmp = name.split("/")[-2]
	cmd = "mrtransform -force -template template_FOD.nii.gz -warp warped_template/"+tmp+"_warpfull2deformation.mif.gz "+name+" transformed_template/"+tmp+"_RK_template.nii.gz"
	print(cmd)
	call(cmd.split(" "))
