import os

# Depth_Prediction 디렉토리 내의 이미지 파일 리스트 가져오기
def depth_txt(depth_prediction_directory):
    image_files = [filename for filename in os.listdir(depth_prediction_directory) if filename.endswith('.png')]

    image_files.sort(key = lambda x: x.split('_')[0])

    # 결과를 저장할 depth_prediction.txt 파일 열기 (덮어쓰기 모드)
    with open('depth_prediction.txt', 'w') as txt_file:
        # 각 이미지에 대해 문자열 생성 및 파일에 쓰기
        for index, filename in enumerate(image_files):
            timestamp_microsecond, _ = os.path.splitext(filename)
            timestamp, microsecond = timestamp_microsecond.split('.')

            # 대응하는 문자열 생성
            output_string = f"{timestamp}.{microsecond[:6]} Depth_Prediction/{index}_depth_norm.jpg"

            # 파일에 쓰기
            txt_file.write(output_string + '\n')

    print("depth_prediction.txt 파일이 생성되었습니다.")

