# coding=UTF-8
import pytesseract
from PIL import Image
from lxml import etree

import time
import os
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
import traceback


# 获取浏览器当前的验证码图片并调用返回验证码
def get_code(driver):
    # 保存浏览器当前页面
    driver.save_screenshot("page.png")
    # 从页面中截取验证码（XPATH定位）
    # vcode = driver.find_element_by_xpath("//*[@id='iframe']")
    # 获取验证码上下左右边界坐标（手动加减像素以更精确）
    # loc = vcode.location
    # size = vcode.size
    # left = loc['x'] + 5
    # top = loc['y']
    # right = (loc['x'] + size['width'] - 5)
    # button = (loc['y'] + size['height'])
    # 截取页面中的验证码（进行截图：参数时一个元组（left,top,right,button）并保存
    page_pic = Image.open('page.png')
    v_code_pic = page_pic.crop((194, 739, 299, 769))
    v_code_pic.save('yzm.png')
    return get_image('yzm.png')


# 自动登录操作(参数为登路账号，密码，webdriver驱动对象)
def login(username, email, password, password2, driver):
    v_code = get_code(driver)
    driver.find_element_by_id('NAME').send_keys(username)  # 自动敲入真实姓名

    driver.find_element_by_id('USERNAME').send_keys(email)  # 自动敲入电子邮箱

    driver.find_element_by_id('PASSWORD').send_keys(password)  # 自动敲入密码

    driver.find_element_by_id('PASSWORD2').send_keys(password2)  # 自动敲入确认密码

    driver.find_element_by_id('auth').send_keys(v_code)  # 自动敲入验证码

    driver.find_element_by_xpath('//*[@id="buttonToSubmit"]').click()


# 灰度化照片后得到验证码
def get_image(name):
    # 打开要识别的图片
    image = Image.open(name)
    image = image.convert('L')
    table1 = []

    # 把图片转化为灰度图像
    for j in range(256):
        if j < 80:
            table1.append(0)
        else:
            table1.append(1)
    image = image.point(table1, '1')
    # 使用pytesseract调用image_to_string方法进行识别，传入要识别的图片，lang='chi_sim'是设置为中文识别，
    # chi_sim 中文
    # eng 英文
    text = pytesseract.image_to_string(image)
    # 输入所识别的文字
    print(1, text)
    return text
