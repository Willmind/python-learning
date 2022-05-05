import pytesseract
from PIL import Image


def demo():
    # 打开要识别的图片
    image = Image.open("test3.png")
    image = image.convert('L')
    table = []

    # 把图片转化为灰度图像
    for i in range(256):
        if i < 80:
            table.append(0)
        else:
            table.append(1)
    image = image.point(table, '1')
    # 使用pytesseract调用image_to_string方法进行识别，传入要识别的图片，lang='chi_sim'是设置为中文识别，
    # chi_sim 中文
    # eng 英文
    text = pytesseract.image_to_string(image)
    # 输入所识别的文字
    print(1, text)


if __name__ == '__main__':
    demo()
