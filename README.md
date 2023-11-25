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



