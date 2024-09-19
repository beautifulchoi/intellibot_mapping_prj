# 필요한 라이브러리 임포트
from collections import defaultdict

def association_txt(rgb_txt_path, depth_prediction_txt_path, association_txt_path):
    # 데이터를 저장할 딕셔너리 초기화
    data_dict = defaultdict(list)

    # rgb.txt 파일 읽기
    with open(rgb_txt_path, 'r') as rgb_file:
        rgb_lines = rgb_file.readlines()

    # depth_prediction.txt 파일 읽기
    with open(depth_prediction_txt_path, 'r') as depth_file:
        depth_lines = depth_file.readlines()

    # rgb.txt의 각 줄에서 timestamp 추출하여 딕셔너리에 저장
    for rgb_line in rgb_lines:
        timestamp = rgb_line.split(' ')[0]
        data_dict[timestamp].append(rgb_line.strip())

    # depth_prediction.txt의 각 줄에서 timestamp 추출하여 딕셔너리에 저장
    for depth_line in depth_lines:
        timestamp = depth_line.split(' ')[0]
        data_dict[timestamp].append(depth_line.strip())

    # association.txt에 timestamp에 대해 정렬하여 데이터 쓰기
    with open(association_txt_path, 'w') as assoc_file:
        for timestamp in sorted(data_dict.keys()):
            combined_string = " ".join(data_dict[timestamp])
            assoc_file.write(combined_string + '\n')

    print("association.txt 파일이 생성되었습니다.")
