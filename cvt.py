print("created by Magnet @ 2024/9/8")
from PIL import Image

def save_image_colors(image_path, output_path, size=(240, 180)):
    # 打开图片
    img = Image.open(image_path)
    
    # 拉伸图片到指定尺寸
    img = img.resize(size)
    
    # 打开输出文件
    with open(output_path, 'w') as file:
        # 遍历每一行
        for y in range(size[1]):
            line_colors = []
            for x in range(size[0]):
                # 获取当前像素的颜色
                pixel = img.getpixel((x, y))
                # 将颜色转换为 FFFFFF 格式
                hex_color = f"{pixel[0]:02X}{pixel[1]:02X}{pixel[2]:02X}"
                line_colors.append(hex_color)
            # 将该行的颜色信息写入文件
            file.write(''.join(line_colors) + '\n')

# 使用示例
image_path = input('input image ')  # 替换为你的图片路径
output_path = input('output ')  # 替换为你想要的输出文件路径
save_image_colors(image_path, output_path)
