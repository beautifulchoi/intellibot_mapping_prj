# Depth estimation with ORB-SLAM2

서울시립대학교 지능형로봇 4조 실습 프로젝트(using nvidia xavider nx and monocular camera) 입니다. 

## 개발 환경
|OS|사용 언어|사용 IDE|
|:---:|:---:|:---:|
|Ubuntu 20.04|C++|visual studio code|

## 프로젝트 개요
1. [ORB-SLAM2](https://github.com/raulmur/ORB_SLAM2) 코드를 웹캠으로 사용할 수 있도록 변형한 [ORB-SLAM2 with WebCamMonocular & RGBD](https://github.com/Taeyoung96/Depth-estimation-with-ORB-SLAM2)를 사용하여 빌드하였습니다.
[블로그 설명글](https://taeyoung96.github.io/slamtip/ORBwithWeb/) 
2. 서울시립대학교 창공관 413호를 비디오 스트림으로 촬영하여 데이터셋 구축  
3. 'Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-shot Cross-dataset Transfer'([Github](https://github.com/isl-org/MiDaS))를 이용하여 RGB Image Sequence에서 Depth map 추출
4. 1번에서 참고하였던 블로그와 유사하게 추출한 predicted depth map을 normailzing


### Code Overview  
- 소스코드는 ORB-SLAM2 및 1번에서 참고하였던 코드와 거의 동일  
- `/Examples/Monocular/mono_tum.cc` : 조건부 컴파일 '#ifdef'를 이용하여 웹캠을 이용할 때와 Sequence 파일을 이용할 때 두 가지 Mode로 구동.  
- `/Examples/RGB-D/rgbd_tum.cc` : 조건부 컴파일 '#ifdef'를 이용하여 'Realsense D435'을 이용할 때와 Sequence 파일을 이용할 때 두 가지 Mode로 구동.  
- `datasets/Depth-prediction-dataset/` : Depth prediction model을 이용하여 구한 Depth data와 그에 맞는 `associations.txt`이 존재.


### trouble shooting
- OpenCV > 2.4.3 not found 에러: orb slam2에서 사용한 opencv는 버전1이지만 최근에는 opencv2를 이용하기 때문에 CMakeList에서 opencv 경로를 제대로 못잡고 있는 문제입니다.([Issue](https://github.com/raulmur/ORB_SLAM2/issues/527
))

CmakeList에서 원래의 opencv버전 경로를 주석처리하고 새로운 버전으로 다운받은 opencv 라이브러리의 패키지 경로로 설정해줍니다. 
```
SET (OpenCV_DIR /usr/include/opencv4)
find_package(OpenCV REQUIRED)
#find_package(OpenCV 3.0 QUIET)
#if(NOT OpenCV_FOUND)
#   find_package(OpenCV 2.4.3 QUIET)
#   if(NOT OpenCV_FOUND)
#      message(FATAL_ERROR "OpenCV > 2.4.3 not found.")
#   endif()
#endif()
```
- #include <opencv/cv.h> 라는 게 없다는 에러: 버전이 opencv2로 업글되어서 그렇습니다. ([Issue](https://github.com/ethz-asl/image_undistort/issues/68))

#include <opencv/cv.h> -> #include <opencv4/opencv2/opencv.hpp>로 바꿔주면 됩니다.

- 엄청난 양의 에러와 함께.. not this scope 뭐시기 에러: c++ 디폴트가 잘못 설정되어 있어 그렇습니다. 다음과 같이 변경해줍니다. ([Issue](https://github.com/UZ-SLAMLab/ORB_SLAM3/issues/387))

```
sed -i 's/++11/++14/g' CMakeLists.txt
```

만약 이렇게 쳤는데도 안된다면,

```
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_EXTENSIONS OFF)
add_definitions(-DCOMPILEDWITHC11)
```
다음과 같이 CmakeList를 변경해줍니다.

- "error: static assertion failed: std::map must have the same value_type as its allocator":다음의 링크를 타고 들어가서 이 사람이 pr날린 것 처럼 변경해줍니다. ([Issue](https://github.com/raulmur/ORB_SLAM2/pull/585/commits))

- cvMat 이 없다~~ 등등 엄청난 에러: opencv 버전 변경 떄문에 그런 것 같습니다. 아래의 코드를 " System.h, pnpsolver.h, sim3solver.h" 에 추가해줍니다. 

```
#include <opencv2/imgproc/types_c.h>
#include <opencv2/opencv.hpp>
using namespace cv;
```

-  ‘CV_LOAD_IMAGE_UNCHANGED’ was not declared in this scope: CV_LOAD_IMAGE_UNCHANGED을 -1로 define 해줍니다([Issue](https://github.com/raulmur/ORB_SLAM2/issues/451))
```
#define CV_LOAD_IMAGE_UNCHANGED= -1
```

- "Pangolin could not be found because dependency Eigen3 could not be found.":pangolin 라이브러리의 버전 변경으로 인한 eigen 라이브러리 호환 문제라고 합니다. cmakelist에서 "find_package(Eigen3 3.1.0 REQUIRED)"를 "find_package(Eigen3 3.1.0 REQUIRED NO_MODULE)" 로 변경([Issue](https://github.com/raulmur/ORB_SLAM2/issues/1015))
