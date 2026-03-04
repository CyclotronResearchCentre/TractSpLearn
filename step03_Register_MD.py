#python Register_MD.py working_directory
#Needs that MD map was named MD_MNI_nii.gz in each patient folder

from glob import glob
import numpy as np
from subprocess import call
import sys

# rep = sys.argv[-1]
rep = "/mnt/data/TractSPlearn/Data"

file_name = glob(rep+ "/*/MD_MNI.nii.gz")
print(file_name)

for name in file_name:
	tmp = name.split("/")[-2]
	cmd = "mrtransform -force -template template_FOD.nii.gz -warp warped_template/"+tmp+"_warpfull2deformation.mif.gz "+name+" transformed_template/"+tmp+"_MD_template.nii.gz"
	print(cmd)
	call(cmd.split(" "))
