###############################################################################
#
# This simple code is video rotating engine for Mac Handbrake
# I had bunch of videos that I wanted to rotate, and could not find any free software for Mac
# So, I made this simple python script that uses HankBrakeCLI to rotates the videos.
# This script will visit the directory you assign, and rotate 90 degree Counter Clockwise every single videos automatically
#
# Authos: Jin Wook Kim (11.04.2015)
# Feel free to modify and use this code. 
# This code follows MIT license.
#
###############################################################################

import os, sys, glob

######################################
# Option. 
# ------------------------------------
# Modify the following values
######################################

# where is video files?
video_path = '/Users/Buster/Desktop/direct_cam'
output_path = '~/Desktop/direct_output/'

# Rotation direction
# If you want counter clockwise, enter 7
# clockwise, enter 4
rotation_direction = '7'


#####################################
# Rotation Code
#####################################
os.chdir(video_path)
for file in glob.glob('*'):
	print "converting : " + file
	file2 = file.replace(' ', '_') # Get rid of all white space 
	os.rename(file, file2)
	cmd = "/Applications/HandBrakeCLI -i ~/Desktop/direct_cam/" + file2 + " -o " + output_path + file2 + " -e x264 -q 20 -B 160 --rotate=" + rotation_direction
	os.system(cmd)

