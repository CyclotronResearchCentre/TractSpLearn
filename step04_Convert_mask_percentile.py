#python Convert_mask_percentile.py N
#Threshold the bundle to get only the 80% top intensity

import os
from glob import glob
import numpy as np
from subprocess import call
import sys

nb = int(sys.argv[-1])



print(nb)


if not os.path.isdir("stat"):
	print("Create folder stat")
	os.mkdir("stat")
else:
	print("Folder stat already exists!")

print(os.getcwd())
file_name = glob("/home/jiqing/postdoc/brian_2024/TractLearn_with_Jinqing/transformed_template/*NoGaussian.nii.gz")
file_name.sort()
print(file_name)

for i in range(nb*300,(nb+1)*300):
	tmp = file_name[i].split("/")[-1].split(".")[0]
	print(tmp)
	cmd = ["mrthreshold", file_name[i], "-percentile", "20","stat/" + tmp+ "_Thr80.mif", "-ignorezero", "-force"]
	print(cmd)
	call(cmd)
