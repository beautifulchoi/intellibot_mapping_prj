import os

def depth_rename(depth_prediction_directory):
    # Depth_Prediction 디렉토리 내의 이미지 파일 리스트 가져오기
    image_files = [filename for filename in os.listdir(depth_prediction_directory) if filename.endswith('.png')]

    image_files.sort(key = lambda x: x.split('_')[0])

    # 각 이미지 파일에 대해 새로운 파일명 생성 및 변경
    for index, filename in enumerate(image_files):
        #timestamp_microsecond, _ = os.path.splitext(filename)
        #timestamp, microsecond = timestamp_microsecond.split('.')

        # 대응하는 새로운 파일명 생성
        new_filename = f"{index}_depth_norm.jpg"

        # 파일 경로 변경
        old_path = os.path.join(depth_prediction_directory, filename)
        new_path = os.path.join(depth_prediction_directory, new_filename)

        # 파일명 변경
        os.rename(old_path, new_path)

    print("Depth_Prediction 파일명이 성공적으로 변경되었습니다.")
