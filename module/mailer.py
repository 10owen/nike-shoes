import os
class Mailer():
    def send_message(self, receivers):
        sender = os.getenv("SENDER_EMAIL")
        sender_pw = os.getenv("SENDER_PW")

        import smtplib
        server = smtplib.SMTP( "smtp.gmail.com", 587 )
        server.starttls()
        server.login(sender, sender_pw)
        from_mail = sender
        body = 'https://www.nike.com/kr/launch/?type=upcoming'

        for receiver in receivers:
            to = receiver
            message = ("From: %s\r\n" % from_mail + "To: %s\r\n" % to + "Subject: %s\r\n" % 'DRAW TIME!' + "\r\n" + body)
            server.sendmail(from_mail, to, message)
    
    def test(self):
        print("this is test function")


if __name__ == "__main__":
    print("this is main")
    mailer = Mailer()
    mailer.test()