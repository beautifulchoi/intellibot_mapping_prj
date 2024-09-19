import cv2
import time
from datetime import datetime
import os

def video_to_image_streams(video_path):
    # 동영상 파일 열기
    cap = cv2.VideoCapture(video_path)

    # 동영상 정보 획득
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 디렉토리 생성
    output_directory = 'rgb'
    os.makedirs(output_directory, exist_ok=True)

    # 각 프레임에 대해 반복
    for frame_number in range(total_frames):
        # 프레임 읽기
        ret, frame = cap.read()
        if not ret:
            break

        # 현재 시간에서 타임스탬프 생성
        timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())

        # 새로운 파일명 생성
        new_filename = os.path.join(output_directory, f"{timestamp}_{frame_number}.jpg")

        # 이미지 저장
        cv2.imwrite(new_filename, frame)

    # 동영상 파일 닫기
    cap.release()

    print('이미지 스트림을 rgb에 저장했습니다.')

# # 예제 동영상 파일 경로
# video_path = 'v1.mp4'

# # video_to_image_streams 함수 호출하여 이미지 스트림들 얻기
# video_to_image_streams(video_path)
