import os
from PIL import Image

# 指定包含图像的文件夹路径
input_folder = "C:\code\shrimp_video\output"
output_folder = "C:\code\shrimp_video\crop"

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取输入文件夹中的所有图像文件
image_files = [f for f in os.listdir(input_folder) if f.endswith((".jpg", ".png", ".jpeg"))]

# 循环处理每张图像
for image_file in image_files:
    # 构建完整的输入图像路径
    input_image_path = os.path.join(input_folder, image_file)
    
    # 打开图像文件
    image = Image.open(input_image_path)

    # 获取图像的宽度和高度
    width, height = image.size

    # 计算要分成两半的宽度
    half_width = width // 2

    # 分割图像
    left_half = image.crop((0, 0, half_width, height))
    right_half = image.crop((half_width, 0, width, height))

    # 构建完整的输出图像路径
    left_output_path = os.path.join(output_folder, f"left_{image_file}")
    right_output_path = os.path.join(output_folder, f"right_{image_file}")

    # 保存分割后的两张图像
    left_half.save(left_output_path)
    right_half.save(right_output_path)

print("图像分割完成。")
