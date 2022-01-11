import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(file_name):
    from_add = 'aliazeem7428@gmail.com'
    to_add = 'nashraislam1999@gmail.com'
    subject = "Finance Stock Report"

    msg = MIMEMultipart()
    msg['From'] = from_add
    msg['To'] = to_add
    msg['Subject'] = subject

    body = "<b>Todays Finance report</b>"
    msg.attach(MIMEText(body,'html'))

    my_file = open(file_name,"rb")

    part = MIMEBase('application','octet-stream')
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment; filename='+file_name)
    msg.attach(part)
    message = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('aliazeem7428@gmail.com','nsrszbnfpgghsfzr')

    server.sendmail(from_add,to_add,message)

    server.quit()