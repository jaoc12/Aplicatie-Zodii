import smtplib, ssl
port = 465
password = input("Enter password: ")
context = ssl.create_default_context()
sender_email = "ttestare35@gmail.com"
f = open(r'''.\lib\Date\date.txt''', "r")
for line in f:
    d = line.split()
    receiver_email = d[0]
    zodie = d[1]
    fisier = r'''.\lib\Zodii''' + '\\' + zodie + '.txt'
    f = open(fisier, "r")
    message = """\
    Subject: Horoscop Zilnic
    
    """
    message = message + f.read()
    message = message.replace('â€“', '-')
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("ttestare35@gmail.com", password)
        server.sendmail(sender_email, receiver_email, message)
f.close()