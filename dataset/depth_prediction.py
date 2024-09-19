import os
import torch
import torchvision.transforms as transforms
from PIL import Image
from tqdm import tqdm

# 이미지 깊이 추정 함수
def depth_estimation(midas, input_image_path, output_depth_map_path):
    # 이미지 로드
    image = Image.open(input_image_path).convert("RGB")

    # 이미지 크기를 MiDaS 모델의 기대 크기로 조정
    transform = transforms.Compose([transforms.Resize((384, 384)), transforms.ToTensor()])
    input_image = transform(image).unsqueeze(0)

    # 추론
    with torch.no_grad():
        prediction = midas(input_image)

    # 결과 크기를 원본 이미지 크기로 조정
    original_size = image.size
    depth_map = prediction.squeeze().cpu().numpy()
    depth_map = (depth_map - depth_map.min()) / (depth_map.max() - depth_map.min()) * 255
    depth_map_image = Image.fromarray(depth_map.astype('uint8')).resize(original_size)
    depth_map_image.save(output_depth_map_path)

def depth_process(midas, input_directory, output_directory):
    # 결과 디렉토리가 없으면 생성
    os.makedirs(output_directory, exist_ok=True)

    # 디렉토리 내의 모든 이미지에 대해 깊이 추정 수행
    for filename in tqdm(os.listdir(input_directory)):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            input_image_path = os.path.join(input_directory, filename)
            output_depth_map_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_depth_map.png")
            depth_estimation(midas, input_image_path, output_depth_map_path)

    print("깊이 추정이 완료되었습니다.")
