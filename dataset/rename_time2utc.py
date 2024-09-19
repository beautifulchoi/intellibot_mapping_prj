# import os
# from datetime import datetime
# import shutil

# def copy_and_rename_images_with_timestamp(directory_path, destination_directory):
#     # output_images 디렉토리에서 파일 목록을 가져오기
#     source_directory = os.path.join(os.getcwd(), directory_path)
#     destination_directory = os.path.join(os.getcwd(), destination_directory)
#     file_list = [filename for filename in os.listdir(source_directory) if os.path.isfile(os.path.join(source_directory, filename))]

#     # 파일들을 타임스탬프로 복사하여 저장하고, 파일명에 대해 오름차순으로 정렬
#     file_list.sort()
#     for filename in file_list:
#         # 현재 파일의 경로와 타겟 경로 설정
#         source_path = os.path.join(source_directory, filename)
#         timestamp = os.path.getmtime(source_path)
#         dt_object = datetime.utcfromtimestamp(timestamp)
#         microsecond_part = dt_object.strftime("%f")  # 마이크로초까지 포함 (소수점 이하 3자리까지)
#         new_filename = f"{int(timestamp)}.{microsecond_part}.jpg"
#         destination_path = os.path.join(destination_directory, new_filename)

#         # 파일 복사
#         shutil.copy2(source_path, destination_path)

# # 함수 호출 (output_images를 new로 복사하고 파일명을 정렬하여 저장)
# copy_and_rename_images_with_timestamp('rgb_test', 'new')

import os
from datetime import datetime
import shutil

def rename_images_with_timestamp(directory_path):
    # 디렉토리에서 파일 목록을 가져오기
    source_directory = os.path.join(os.getcwd(), directory_path)
    file_list = [filename for filename in os.listdir(source_directory) if os.path.isfile(os.path.join(source_directory, filename))]

    # 파일들을 타임스탬프로 변경하여 저장
    file_list.sort()
    for filename in file_list:
        # 현재 파일의 경로 설정
        source_path = os.path.join(source_directory, filename)
        timestamp = os.path.getmtime(source_path)
        dt_object = datetime.utcfromtimestamp(timestamp)
        microsecond_part = dt_object.strftime("%f")  # 마이크로초까지 포함 (소수점 이하 3자리까지)
        new_filename = f"{int(timestamp)}.{microsecond_part}.jpg"
        new_path = os.path.join(source_directory, new_filename)

        # 파일 이름 변경 (덮어쓰기)
        os.rename(source_path, new_path)

    print('rgb 파일들의 이름이 변경되었습니다.')

# # 함수 호출 (rgb_test 디렉토리의 파일명을 변경하여 덮어쓰기)
# rename_images_with_timestamp('rgb_test')
