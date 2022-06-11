from flask import *
from flask_recaptcha import ReCaptcha

from Ceasar import decrypt
from json_handler import read, write
from menu import menu

path = "config_activation.json"

app = Flask(__name__)
app.config['RECAPTCHA_SITE_KEY'] = '6LfyndAfAAAAAHb24rWq_APs6NrNcX00tPyvOm_y'
app.config['RECAPTCHA_SECRET_KEY'] = '6LfyndAfAAAAAA84oVjR0OQx6twdoo25SYMR_Rox'
app.config['RECAPTCHA_DISABLE'] = False
recaptcha = ReCaptcha(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        if recaptcha.verify():
            message = 'Thanks for filling out the ReCaptcha! \n Now, please, enter activation code in console'
            activator()
        else:
            message = 'Please fill out the ReCaptcha!'
    return render_template('index.html', message=message)


def activator():

    config = read(path)
    code = str(input("Enter activation code: "))
    if (code == decrypt(config.get("code"), 3)):
        print("Activation Success!")
        config["activated"] = True
        write(path, config)
        menu()
    else:
        print("Invalid activation code!")
        activator()
