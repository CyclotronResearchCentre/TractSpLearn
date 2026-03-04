#python Register_TWI_FOD.py argument 0 (postprocess patient 1 to 10) or 1 (11 to 20)

from glob import glob
from subprocess import call
import sys
import os

# if len(sys.argv) == 4:
# 	file_name = glob("transformed_template/"+sys.argv[-2]+"*.mif.gz")
# else:
# 	file_name = glob("transformed_template/*.mif.gz")
file_name= glob("/home/jiqing/postdoc/brian_2024/TractLearn_with_Jinqing/transformed_template/*.mif.gz")

#print(file_name)
file_name.sort()
print(file_name)
print(sys.argv)



# for name in file_name[s*10:(s+1)*10]:
for name in file_name:
	print(name)
	tmp = name.split("/")[-1].split("_transformed.")[0]
	tmp_track = glob("/home/jiqing/postdoc/brian_2024/TractLearn_with_Jinqing/transformed_template/"+tmp+"*.tck")
	print(tmp)
	print(tmp_track)
	for track in tmp_track:
		track_tmp = track.split(".")[0]
		print(track)
		toCreate = track_tmp+"_TW_FOD_Gaussian.nii.gz"
		#if 1==1:
		# if not os.path.exists(toCreate):
		if not os.path.exists(toCreate) :
			cmd = "tckmap "+track+" -stat_tck gaussian -fwhm_tck 8 -template template_FOD.nii.gz -contrast fod_amp -force -image "+name+" -stat_vox mean "+track_tmp+"_TW_FOD_Gaussian.nii.gz"
			print(cmd)
			call(cmd.split(" "))
			cmd = "tckmap "+track+" "+track_tmp+"_TDI_NoGaussian.nii.gz -template template_FOD.nii.gz -force"
			call(cmd.split(" "))
			cmd = "tckmap "+track+" -stat_tck gaussian -fwhm_tck 8 -template template_FOD.nii.gz -contrast scalar_map -image transformed_template/"+tmp+"_FA_template.nii.gz -force -stat_vox mean "+track_tmp+"_TW_FA_Gaussian.nii.gz"
			print(cmd)
			call(cmd.split(" "))
			cmd = "mrcalc -force "+track_tmp+"_TW_FOD_Gaussian.nii.gz 0 -gt transformed_template/"+tmp+"_FA_template.nii.gz -mult "+track_tmp+"_Fractional_Gaussian.nii.gz"
			print(cmd)
			call(cmd.split(" "))
			cmd = "afdconnectivity -afd_map "+track_tmp+"_AFD_Gaussian.nii.gz "+name+" "+track
			print(cmd)
			call(cmd.split(" "))
			cmd = "tckmap "+track+" -stat_tck gaussian -fwhm_tck 8 -template template_FOD.nii.gz -contrast scalar_map -image transformed_template/"+tmp+"_MD_template.nii.gz -force -stat_vox mean "+track_tmp+"_TW_MD_Gaussian.nii.gz"
			print(cmd)
			call(cmd.split(" "))
			cmd = "mrcalc -force "+track_tmp+"_TW_FOD_Gaussian.nii.gz 0 -gt transformed_template/"+tmp+"_MD_template.nii.gz -mult "+track_tmp+"_Fractional_Gaussian.nii.gz"
			print(cmd)
			call(cmd.split(" "))
			cmd = "tckmap "+track+" -stat_tck gaussian -fwhm_tck 8 -template template_FOD.nii.gz -contrast scalar_map -image transformed_template/"+tmp+"_AD_template.nii.gz -force -stat_vox mean "+track_tmp+"_TW_AD_Gaussian.nii.gz"
			print(cmd)
			call(cmd.split(" "))
			cmd = "mrcalc -force "+track_tmp+"_TW_FOD_Gaussian.nii.gz 0 -gt transformed_template/"+tmp+"_AD_template.nii.gz -mult "+track_tmp+"_Fractional_Gaussian.nii.gz"
			print(cmd)
			call(cmd.split(" "))
			cmd = "tckmap "+track+" -stat_tck gaussian -fwhm_tck 8 -template template_FOD.nii.gz -contrast scalar_map -image transformed_template/"+tmp+"_RD_template.nii.gz -force -stat_vox mean "+track_tmp+"_TW_RD_Gaussian.nii.gz"
			print(cmd)
			call(cmd.split(" "))
			cmd = "mrcalc -force "+track_tmp+"_TW_FOD_Gaussian.nii.gz 0 -gt transformed_template/"+tmp+"_RD_template.nii.gz -mult "+track_tmp+"_Fractional_Gaussian.nii.gz"
			print(cmd)
			call(cmd.split(" "))
			cmd = "tckmap "+track+" -stat_tck gaussian -fwhm_tck 8 -template template_FOD.nii.gz -contrast scalar_map -image transformed_template/"+tmp+"_AK_template.nii.gz -force -stat_vox mean "+track_tmp+"_TW_AK_Gaussian.nii.gz"
			print(cmd)
			call(cmd.split(" "))
			cmd = "mrcalc -force "+track_tmp+"_TW_FOD_Gaussian.nii.gz 0 -gt transformed_template/"+tmp+"_AK_template.nii.gz -mult "+track_tmp+"_Fractional_Gaussian.nii.gz"
			print(cmd)
			call(cmd.split(" "))
			cmd = "tckmap "+track+" -stat_tck gaussian -fwhm_tck 8 -template template_FOD.nii.gz -contrast scalar_map -image transformed_template/"+tmp+"_MK_template.nii.gz -force -stat_vox mean "+track_tmp+"_TW_MK_Gaussian.nii.gz"
			print(cmd)
			call(cmd.split(" "))
			cmd = "mrcalc -force "+track_tmp+"_TW_FOD_Gaussian.nii.gz 0 -gt transformed_template/"+tmp+"_MK_template.nii.gz -mult "+track_tmp+"_Fractional_Gaussian.nii.gz"
			print(cmd)
			call(cmd.split(" "))
			cmd = "tckmap "+track+" -stat_tck gaussian -fwhm_tck 8 -template template_FOD.nii.gz -contrast scalar_map -image transformed_template/"+tmp+"_RK_template.nii.gz -force -stat_vox mean "+track_tmp+"_TW_RK_Gaussian.nii.gz"
			print(cmd)
			call(cmd.split(" "))
			cmd = "mrcalc -force "+track_tmp+"_TW_FOD_Gaussian.nii.gz 0 -gt transformed_template/"+tmp+"_RK_template.nii.gz -mult "+track_tmp+"_Fractional_Gaussian.nii.gz"
