import image_stream as rgb_process
import rename_time2utc as rgb_rename
import txt_rgb as rgb_txt

import depth_prediction as depth_process
import txt_depth as depth_txt
import rename_depth_time2index as depth_rename

import txt_association

import torch

# 예제 동영상 파일 경로
video_path = 'v1.mp4'

# 비디오 파일에서 이미지 스트림을 얻어내 rgb 디렉토리에 저장
rgb_process.video_to_image_streams(video_path)

# rgb 디렉토리에서 datetime format으로 작명된 파일들을 ufc format으로 변환
rgb_rename.rename_images_with_timestamp('rgb')

# rgb 디렉토리의 파일들로 부터 txt 파일 생성
rgb_txt.create_rgb_txt_from_rgb_directory('rgb')

# rgb 디렉토리의 파일들로 부터 depth-estimation 파일들을 depth_prediction에 저장
midas = torch.hub.load("intel-isl/MiDaS", "MiDaS")
depth_process.depth_process(midas, 'rgb', 'Depth_Prediction')

# timestamp로 시작한 depth-estimation 파일들로부터 txt를 형성
depth_txt.depth_txt('Depth_Prediction')

# timestamp를 얻어냈으니 index_depth_norm꼴로 이름 변경
depth_rename.depth_rename('Depth_Prediction')

# rgb.txt와 depth_prediction.txt파일로 부터 associate.txt 생성
txt_association.association_txt("rgb.txt", "depth_prediction.txt", "association.txt")