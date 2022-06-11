import os
import random
# from random import randint
# from PIL import Image as image, ImageDraw as imagedraw, ImageFont as imagefont
from flask import *
#
# # from ReCaptchaa import activator
from ReCaptchaa import activator
#
app = Flask(__name__)
#
#
# def get_random_color():
#     # Random color rgb
#     return randint(120, 200), randint(120, 200), randint(120, 200)
#
#
# def get_random_code():
#     # Random characters
#     codes = [[chr(i) for i in range(48, 58)], [chr(i) for i in range(65, 91)], [chr(i) for i in range(97, 123)]]
#     codes = codes[randint(0, 2)]
#     return codes[randint(0, len(codes) - 1)]
#
#
# def generate_captcha(width=140, height=60, length=4):
#     # Generate verification code
#     img = image.new("RGB", (width, height), color=get_random_color())
#     draw = imagedraw.Draw(img)
#     font = imagefont.truetype("font/321impact.ttf", size=36)
#     # Captcha text
#     text = ""
#     for i in range(length):
#         c = get_random_code()
#         text += c
#         rand_len = randint(-5, 5)
#         draw.text((width * 0.2 * (i + 1) + rand_len, height * 0.2 + rand_len), c, font=font, fill=get_random_color())
#     # Add interference line
#     for i in range(3):
#         x1 = randint(0, width)
#         y1 = randint(0, height)
#         x2 = randint(0, width)
#         y2 = randint(0, height)
#         draw.line((x1, y1, x2, y2), fill=get_random_color())
#     # Add interference points
#     for i in range(16):
#         draw.point((randint(0, width), randint(0, height)), fill=get_random_color())
#     # save Picture
#     img.save("static\\images\\captcha\\" + text + ".jpg")
#     return text + ".jpg"


# if __name__ == "__main__":
#     for i in range(1000):
#         generate_captcha()


@app.route("/", methods=["get", "post"])
def get_captcha():
    list = os.listdir("static/images/captcha")
    img = list[random.randint(0, 1000)]
    rec = str(str(os.path.join("static\\images\\captcha", img)).removeprefix("templates\\").replace("\\", "/"))
    name = img.removesuffix(".jpg")
    return render_template('indexx.html',
                           recaptcha=rec,
                           captch=name
                           )


@app.route("/captcha_success", methods=["get", "post"])
def success():
    activator()


#
# print("Follow the link and solve captcha to enter the activation code")
# app.run(debug=False, use_evalex=False)
