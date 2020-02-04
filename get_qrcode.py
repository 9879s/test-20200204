#!/usr/bin/python3
import qrcode

#想要生成的二维码
text = "https://www.baidu.com"

# 生成二维码
img = qrcode.make(data=text)

# 直接显示二维码
img.show()

# 保存二维码为文件
img.save("show_qrcode.jpg")

