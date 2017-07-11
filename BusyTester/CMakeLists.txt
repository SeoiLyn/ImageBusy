CMAKE_MINIMUM_REQUIRED(VERSION 2.8)
if(COMMAND cmake_policy)
      cmake_policy(SET CMP0003 NEW)
endif(COMMAND cmake_policy)

PROJECT(BusyTester)

if( WIN32 )
    add_definitions(-D_CRT_SECURE_NO_WARNINGS)
    add_definitions(-DUNICODE -D_UNICODE)
endif( WIN32 )

FIND_PACKAGE( OpenCV REQUIRED )
FIND_PACKAGE(Boost REQUIRED)
#FIND_PACKAGE(BerkeleyDB REQUIRED)

include_directories(${Boost_INCLUDE_DIR})
include_directories(${BusyTester_SOURCE_DIR}/../)

link_directories(${BusyTester_SOURCE_DIR}/SDK)
link_directories(${Boost_LIBRARY_DIR})

if( WIN32 )
    SET(SRC_LIST main.cpp)
else( WIN32 )
    SET(SRC_LIST main.cpp)
endif( WIN32 )

SET(LINK_TARGET_EXE BusyTester)

add_executable(${LINK_TARGET_EXE} ${SRC_LIST})

#TARGET_LINK_LIBRARIES(${LINK_TARGET_EXE} ${BerkeleyDB_LIBRARIES})
TARGET_LINK_LIBRARIES(${LINK_TARGET_EXE} ${OpenCV_LIBS})
TARGET_LINK_LIBRARIES(${LINK_TARGET_EXE} ${Boost_LIBRARIES})

if( WIN32 )
    TARGET_LINK_LIBRARIES(${LINK_TARGET_EXE} ${Boost_LIBRARIES})
    TARGET_LINK_LIBRARIES(${LINK_TARGET_EXE} ${OpenCV_LIBRARIES_Win})
else( WIN32 )
    TARGET_LINK_LIBRARIES(ClipperKernel ${Boost_LIBRARIES})
    TARGET_LINK_LIBRARIES(${LINK_TARGET_EXE} boost_filesystem boost_thread boost_system)
    TARGET_LINK_LIBRARIES(${LINK_TARGET_EXE} opencv_calib3d opencv_contrib opencv_core opencv_features2d opencv_flann opencv_gpu opencv_highgui opencv_imgproc opencv_legacy opencv_ml opencv_nonfree opencv_objdetect opencv_photo opencv_stitching opencv_ts opencv_video opencv_videostab)
endif( WIN32 )
