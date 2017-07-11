CMAKE_MINIMUM_REQUIRED(VERSION 2.8)
if(COMMAND cmake_policy)
      cmake_policy(SET CMP0003 NEW)
endif(COMMAND cmake_policy)

PROJECT(ImageBusy)

SET(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR})
SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}) 
SET(CMAKE_DEBUG_POSTFIX d)

message(STATUS "Target platform: " "CMAKE_CXX_COMPILER_VERSION")

if ( WIN32 )
    message(${BOOST_ROOT_SET})
    set(BOOST_ROOT ${BOOST_ROOT_SET})
    set(OpenCV_DIR ${OPENCV_ROOT_SET})

    if (MSVC14)
        #use VS 2015
        message("using Visual Studio 2015")
    else (MSVC14)
        #use VS 2008
        message("using Visual Studio 2008")
    endif(MSVC14)
      
    set(FFMPEG_INCLUDE_DIR ${FFMPEG_ROOT_SET}/include)
    set(FFMPEG_LIBRARY_DIR ${FFMPEG_ROOT_SET}/lib)
    
else ( WIN32 )
    #set(Boost_INCLUDE_DIR /usr/local/include)
    #set(Boost_LIBRARY_DIR /usr/local/lib)
    set(FFMPEG_INCLUDE_DIR /usr/local/include)
    set(FFMPEG_LIBRARY_DIR /usr/local/lib)
endif( WIN32 )

FIND_PACKAGE( OpenCV REQUIRED )
find_package(Boost REQUIRED)

include_directories(${Boost_INCLUDE_DIR})
include_directories(${ImageBusy_SOURCE_DIR}/)
link_directories(${OpenCV_LIB_DIR})

include_directories(${FFMPEG_INCLUDE_DIR})
link_directories(${FFMPEG_LIBRARY_DIR})

if ( WIN32 )
    link_directories(${Boost_LIBRARY_DIRS})
endif( WIN32 )

SET (FFMPEG_LIBRARIES
  avcodec
  avdevice
  avfilter
  avformat
  avutil
  postproc
  swresample
  swscale
 )

add_subdirectory(./BusyTester)