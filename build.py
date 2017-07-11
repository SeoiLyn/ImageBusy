#!/usr/bin/python 
# -*- coding:utf-8 -*-
#python 2.7.x

import os
import shutil
import ConfigParser
import zipfile,os.path
import platform

VS_VERSION_9 = "Visual Studio 9 2008"
VS_VERSION_9_x64 = "Visual Studio 9 2008 Win64"
VS_VERSION_14 = "Visual Studio 14 2015"
VS_VERSION_14_x64 = "Visual Studio 14 2015 Win64"

#define FFMPEG win32 & win64 version
#FFMPEG_WIN32_VERSION = "ffmpeg-3.2.4-win32"
#FFMPEG_WIN64_VERSION = "ffmpeg-3.2.4-win64"
FFMPEG_WIN32_VERSION = "ffmpeg-2.2.1-win32"
FFMPEG_WIN64_VERSION = "ffmpeg-2.8.3-win64"

def copy_files(path, target):
    # returns a list of names (with extension, without full path) of all files 
    # in folder path
    #files = []
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            #files.append(name)
            shutil.copy(os.path.join(path, name), os.path.join(path,target))
    #return files 

#for Windows cmake project usage
def Windows_cmake():

    vs_choice = raw_input("Select Visual studio version(1 for VS2008 32bit, 2 for VS2008 64bit, 3 for VS2015 32bit, 4 for VS2015 64bit)?")

    if (vs_choice == '1'):
        VS_VERSION = VS_VERSION_9
    elif (vs_choice == '2'):
        VS_VERSION = VS_VERSION_9_x64
    elif (vs_choice == '3'):
        VS_VERSION = VS_VERSION_14
    elif (vs_choice == '4'):
        VS_VERSION = VS_VERSION_14_x64
    else:
        VS_VERSION = VS_VERSION_9
    
    path = os.getcwd()
    os.chdir(path)
    
    #create depends folder
    shadow = path+"/shadow"
    if os.path.exists(shadow):
        shutil.rmtree(shadow)
    os.makedirs(shadow)
   
    os.chdir(shadow)


    #2.4.12 support VS2008 32bit&64bit, VS2015 32bit
    #OPENCV_ROOT = "D:/OpenSource/OpenCV-2.4.12/install/"
    #if want to use opencv 3.1.0, support VS2015 64bit
    OPENCV_ROOT = "D:/OpenSource/OpenCV-3.1.0/install/"

    if (VS_VERSION == VS_VERSION_14):
        opencv_bin = OPENCV_ROOT + "/x86/vc14/bin/"
        FFMPEG_ROOT = "D:/OpenSource/" + FFMPEG_WIN32_VERSION
        BOOST_ROOT = "D:/OpenSource/boost_1_58_0"
    elif (VS_VERSION == VS_VERSION_14_x64):
        opencv_bin = OPENCV_ROOT + "/x64/vc14/bin/"
        FFMPEG_ROOT = "D:/OpenSource/" + FFMPEG_WIN64_VERSION
        BOOST_ROOT = "D:/OpenSource/boost_1_58_0_x64"
    elif (VS_VERSION == VS_VERSION_9_x64):
        opencv_bin = OPENCV_ROOT + "/x64/vc9/bin/"
        FFMPEG_ROOT = "D:/OpenSource/" + FFMPEG_WIN64_VERSION
        BOOST_ROOT = "D:/OpenSource/boost_1_58_0_x64"
    else:
        #default for VS2008 32bit
        opencv_bin = OPENCV_ROOT + "/x86/vc9/bin/"
        FFMPEG_ROOT = "D:/OpenSource/"+FFMPEG_WIN32_VERSION
        BOOST_ROOT = "D:/OpenSource/boost_1_58_0"
    
    #CMAKE_COMMAND = "cmake-gui -G \""+VS_VERSION+"\" -DBOOST_ROOT_SET:STRING="+BOOST_ROOT+" -DOPENCV_ROOT_SET:STRING="+OPENCV_ROOT+" -DFFMPEG_ROOT_SET:STRING="+FFMPEG_ROOT+" ../"
    CMAKE_COMMAND = "cmake -G \""+VS_VERSION+"\" -DBOOST_ROOT_SET:STRING="+BOOST_ROOT+" -DOPENCV_ROOT_SET:STRING="+OPENCV_ROOT+" -DFFMPEG_ROOT_SET:STRING="+FFMPEG_ROOT+" ../"
    os.system(CMAKE_COMMAND)
        
    #try to copy dlls
    shadowDebugDir = shadow+"/Debug"
    os.makedirs(shadowDebugDir)
    os.chmod(shadowDebugDir, 0o777)
    
    shadowReleaseDir = shadow+"/Release"
    os.makedirs(shadowReleaseDir)
    os.chmod(shadowReleaseDir, 0o777)

    #copy files
    copy_files(opencv_bin, shadowReleaseDir)
    copy_files(opencv_bin, shadowDebugDir)

    #log4cxx_bin = LOG4CXX_ROOT + "/lib/"
    #copy_files(log4cxx_bin, shadowReleaseDir)
    #copy_files(log4cxx_bin, shadowDebugDir)

    ffmpeg_bin = FFMPEG_ROOT + "/bin/"
    copy_files(ffmpeg_bin, shadowReleaseDir)
    copy_files(ffmpeg_bin, shadowDebugDir)

    choice = raw_input("Do you want to open ImageBusy.sln(y/n, default to n)?")
    if choice == 'y' :
        os.startfile(shadow+"/ImageBusy.sln")

def Linux_cmake():
    path = os.getcwd()

    #create depends folder
    shadow = path+"/shadow"
    if os.path.exists(shadow):
        shutil.rmtree(shadow)
    os.makedirs(shadow)
   
    os.chdir(shadow)

    CMAKE_COMMAND = "cmake ../"
    os.system(CMAKE_COMMAND)

def Apple_cmake():
    path = os.getcwd()
    
    #create depends folder
    shadow = path+"/shadow"
    if os.path.exists(shadow):
        shutil.rmtree(shadow)
    os.makedirs(shadow)

    os.chdir(shadow)
    
    CMAKE_COMMAND = "cmake-gui ../"
    os.system(CMAKE_COMMAND)
        
if __name__ == "__main__":

    if platform.system() == "Windows":
        print "system is Windows"
        Windows_cmake()
    elif platform.system() == "Darwin":
        print "system is Mac"
        Apple_cmake()
    elif platform.system() == "linux":
        print "system is Linux"
        Linux_cmake()
    else:
        print "system is unknow! the name is: "+platform.system();
