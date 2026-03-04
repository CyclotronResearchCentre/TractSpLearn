#python Register_FA.py working_directory
#Needs that FA map was named FA_MNI_nii.gz in each patient folder

from glob import glob
import numpy as np
from subprocess import call
import sys
import os

# rep = sys.argv[-1]
rep = "/mnt/data/TractSPlearn/Data"

file_name = glob(rep+ "/*/FA_MNI.nii.gz")
print(file_name)

for name in file_name:
	tmp = name.split("/")[-2]
	# cmd = "mrtransform -force -template template_FOD.nii.gz -warp /home/jiqing/postdoc/brian_2024/TractLearn_with_Jinqing/warped_template/"+tmp+"_warpfull2deformation.mif.gz "+name+" /home/jiqing/postdoc/brian_2024/TractLearn_with_Jinqing/transformed_template/"+tmp+"_FA_template.nii.gz"
	cmd = "mrtransform -force -template template_FOD.nii.gz -warp warped_template/"+tmp+"_warpfull2deformation.mif.gz "+name+" transformed_template/"+tmp+"_FA_template.nii.gz"
	print(cmd)
	# print(os.getcwd())
	call(cmd.split(" "))
