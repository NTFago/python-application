from PIL import Image, ImageDraw
import numpy as np
import cv2

def img2char(imgobj):
    scale = 5
    # 图片宽高
    width, height = (int(imgobj.width/scale), int(imgobj.height/scale))
    # 灰度图
    img_original = imgobj.resize((width, height))
    img = imgobj.convert('L').resize((width, height))
    # 70 level 字符串
    ASCII_HIGH = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. '''
    # 字符串转图片
    img_new = Image.new('RGB', (width*scale, height*scale), 'white')  # 生成空白图
    draw = ImageDraw.Draw(img_new)  # 图片转画布
    # 灰度转字符串
    for y in range(height):
        for x in range(width):
            pos = (x, y)
            gray = img.getpixel(pos)
            index = int(gray/256*70)
            txt = ASCII_HIGH[index] + ' '
            color = img_original.getpixel(pos)
            draw.text((x*scale, y*scale), txt, fill=color)

    return img_new

cap = cv2.VideoCapture("请好好看着我.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)     # FPS信息
# 宽高信息
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width, height)
# 帧总数
frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

videoWriter = cv2.VideoWriter("char.mp4", cv2.VideoWriter_fourcc(*"MP4V"), fps, size)

ret, frame = cap.read()

index = 1

while ret:
    print(f"正在处理第{index}帧/共{frameCount}帧")
    frame_pic = Image.fromarray(frame)
    char_pic = img2char(frame_pic)
    char_pic.save(f"D://一些东东/project/请好好看着我/分帧/第{index}帧.png")
    mat_pic = np.array(char_pic)
    videoWriter.write(mat_pic)

    ret, frame = cap.read()
    index += 1

cap.release()
