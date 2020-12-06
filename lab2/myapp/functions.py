import json
import smtplib
from random import *

userdata = {
  "users_list": [
      {
          "login": "yulia",
          "e-mail": "randomemailkek1@mail.ru",
          "password": "some_password",
          "code": "4242"
      }
   ]
}

json_file = open("userdata.json", "w")
json.dump(userdata, json_file)
json_file.close()


def find_user(login, password):
    # json_file = json.load(open("userdata.json", "w"))
    # json.dump(userdata, json_file)
    # json_file.close()

    userdata = json.load(open("userdata.json", "r"))
    if userdata["users_list"][0]["login"] == login:
        if userdata["users_list"][0]["password"] == password:
            email = userdata["users_list"][0]["e-mail"]
            return email
        else:
            return "Wrong password"
    else:
        return "User not found"



def send_code(email):
    code = get_code(length=4)
    server_email = "server333777@gmail.com"
    server_password = 'hCkeME5qZNWeuqf'
    addressee = email
    mail_title = "Code"
    mail_text = "Code: " + code
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (server_email, ", ".join(addressee), mail_title, mail_text)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(server_email, server_password)
        server.sendmail(server_email, addressee, message)
        server.close()
    except Exception:
        return "Что-то пошло не так"
    dump_code(code)


def dump_code(code):
    open_file = open("userdata.json", "r")
    json_file = json.load(open_file)
    json_file["users_list"][0]["code"] = code
    open_file.close()

    open_file = open("userdata.json", "w")
    json.dump(json_file, open_file)
    open_file.close()


def authentication(code):
    open_file = open("userdata.json", "r")
    json_file = json.load(open_file)
    if json_file["users_list"][0]["code"] == code:
        open_file.close()
        return "auth_ok"
    else:
        open_file.close()
        return None


def get_code(length=4):
    code = ''
    for i in range(0, length):
        d = randint(0, 9)
        code += str(d)
    return code
