import os

def create_rgb_txt_from_rgb_directory(directory_path):
    # new 디렉토리에서 파일 목록을 가져오기
    new_directory = os.path.join(os.getcwd(), directory_path)
    file_list = [filename for filename in os.listdir(new_directory) if os.path.isfile(os.path.join(new_directory, filename))]

    # 파일명을 오름차순으로 정렬
    file_list.sort()

    # 결과를 저장할 txt 파일 생성 또는 열기 (덮어쓰기 모드)
    with open('rgb.txt', 'w') as txt_file:
        # 각 파일에 대해 '파일명 rgb/파일명.jpg' 형식으로 문자열 작성 및 파일에 쓰기
        for filename in file_list:
            base_name, extension = os.path.splitext(filename)
            rgb_format = f"{base_name} rgb/{filename}"
            txt_file.write(rgb_format + '\n')

    print("rgb.txt 파일이 생성되었습니다.")

# # new 디렉토리를 대상으로 함수 호출
# create_rgb_txt_from_new_directory('rgb_test')
