from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
import requests
import re


if __name__ == "__main__":
    active_ip = None
    try:
        active_ip = requests.get(url='https://www.whatismyip.com/').text
    except:
        print(">> Error fetching site, aborting...")
        raise SystemExit

    prev_ip = None
    with open('Prev_IP.txt', 'r') as f:
        try:
            prev_ip = f.read().strip()
        except FileNotFoundError:
            new_file = open('Prev_IP.txt', 'a')
            new_file.close()

    if prev_ip == active_ip:
        print(">> IP not changed")
    else:
        with open('Prev_IP.txt', 'w') as f:
            f.write(active_ip)
        html_Mail_Body = f'''
        <HTML>
            <BODY>
                <h4 align="left">
                    Dear Recipient, <br>Your Public IP has changed, thus the e-mail<br>
                </h4>
                <h5>OLD IP : {prev_ip}</h5>
                <h5>NEW IP : {active_ip}</h5>
                <h4>Best Wishes..<br>Your Automator!</h4>        
            </BODY>
        </HTML>
        '''

        msg = MIMEMultipart('alternative')
        msg['Subject'] = f"New Public IP : {active_ip}"
        msg['From'] = "akashofficial1998@gmail.com"
        msg['To'] = "idioticpanda@hotmail.com"
        msg.attach(MIMEText(html_Mail_Body, 'html'))

        try:
            s = SMTP('smtp.gmail.com', '587')
            s.starttls()
            s.login('akashofficial1998@gmail.com', '')
            s.sendmail('akashofficial1998@gmail.com', 'idioticpanda@hotmail.com', msg.as_string())
        except:
            print(">> Unable to send mail!")

