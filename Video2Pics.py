"""
Created on Tue Feb 23 11:09:49 2021

@author: premkm
"""

import cv2
import os
import sys
from datetime import datetime as dtm
import numpy as np
class Video2Pics:
    def __init__(self,
                 video_srcpath,
                 start_time=None,
                 end_time=None,
                 frame_rate=None,
                 save_format="jpg",
                 output_dir=None):
        

        self.video_srcpath = video_srcpath #source path of the file
        self.start_time = start_time #start time of video in secs
        self.end_time = end_time #end time of video in secs
        self.frame_rate = frame_rate #frame rate to capture the pictures
        self.save_format = save_format #save format of the file
        self.output_dir = output_dir #output dir to save the pictures

    #defult value assign for parameters missing assignment
    # assign the soruce path for generating the pictures if output dir not assigned
        if not self.output_dir:
            self.output_dir = '/'.join(video_srcpath.split(os.path.sep)[:-1])+'/'
        else:
            self.output_dir = '/'.join(output_dir.split(os.path.sep)[:-1])+'/'
    
    # assign the default start time to 0
        if not self.start_time:
            self.start_time = 0

        #date time for the file generated to save file name
        self.dt=dtm.now().strftime("%Y_%m_%d-%I_%M_%S_")
        self.vidcap = cv2.VideoCapture(video_srcpath)#create the cv2 object to capture the image
        self.video_filename = video_srcpath.split(os.path.sep)[-1]#extract the source file name
        if(self.vidcap.isOpened() == False):
            sys.exit("Error: the file is unvailable")
       
        if not self.end_time:
            fr,self.end_time = self.getVideoDetails() 
		
        self.fr,et=self.getVideoDetails()
		
        if self.frame_rate:
            if (self.frame_rate*1000) < (self.fr):
               sys.exit(" frame_rate is greater than FPS ")
			
			
        #frame rate assigned 
        if not self.frame_rate:
            self.frame_rate,et=self.getVideoDetails()

        if self.frame_rate <= 0:
            sys.exit(" Frame capture rate shoud be > 0 ")
		
        # Extracting extension of input vide file
        file_extension = self.video_filename.split(".")[-1]

        # Valid Video Extensions
        VIDEO_EXTENSIONS = ["mov", "avi", "mpg", "mpeg", "mp4", "mkv", "wmv"]

        # Valid Output Picture Extension
        PIC_EXTENSIONS = ["jpg", "png", "jpeg", "bmp", "tiff", "tif", "dicom", "dcm"]

        if file_extension not in VIDEO_EXTENSIONS:
            sys.exit(" Invalid video file ")


        if not self.save_format:
            self.save_format = 'jpg'

        # Checking for valid output image file extension format
        if self.save_format not in PIC_EXTENSIONS:
            sys.exit(" image format not supported ")

        fr,ed=self.getVideoDetails()
        #print the video details
        print('fps = ' + str(self.fps))
        print('number of frames = ' + str(self.frame_count))
        print('duration (M:S) = ' + str(self.minutes) + ':' + str(self.seconds))
        self.sec = int(self.start_time)
        #get the position of the video
        self.frame_time=self.vidcap.get(cv2.CAP_PROP_POS_MSEC)
        print("Start time",self.start_time)
        print("End time",self.end_time)
        print("Frame rate",self.frame_rate)
        self.frameRate = int(self.frame_rate) 
        self.count=0
        success = self.getFramePic(self.sec) #read the video file and generate images
        while success and int(self.start_time)<int(self.end_time):
            self.count = self.count + 1
            self.sec = self.sec + float(self.frame_rate)
            success = self.getFramePic(self.sec)
            self.sec = round(self.sec, 2)            
            self.start_time = (self.vidcap.get(cv2.CAP_PROP_POS_MSEC)/1000) #get the current position

        print("Total Number of Images",self.count) 

#fuction to get the basic video details
    def getVideoDetails(self):
        if not self.video_filename:
            sys.exit(" File doesnot exists ")
        
        file_extension = self.video_filename.split(".")[-1]
       #get the video details 
        self.fps = self.vidcap.get(cv2.CAP_PROP_FPS)      # frames per second video
        self.frame_count = int(self.vidcap.get(cv2.CAP_PROP_FRAME_COUNT)) 
        self.duration = self.frame_count/self.fps #duration of video file
       
        self.minutes = int(self.duration/60)
        self.seconds = self.duration%60
        
        return self.fps,self.duration    
    

#function to capture the frames and convert to images
    def getFramePic(self,sec):
        self.vidcap.set(cv2.CAP_PROP_POS_MSEC,self.sec*1000) #set the position
        hasFrames,image = self.vidcap.read()      #read and generate the image
        if hasFrames:
            cv2.imwrite(str(self.output_dir)+"pic_"+str(self.dt)+str(self.count)+"."+self.save_format, image) # save frame as picture
        return hasFrames


