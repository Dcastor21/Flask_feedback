import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port =2525
    smtp_server= 'smtp.mailtrap.io'
    login ='c8d6a633250aff'
    password='1cecdb1b724f79'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"



    sender_email = 'darnelcastor2@gmail.com'
    receiver_email = 'castordarnel6@gmail.com'
    msg = MIMEText(message, 'html')
    msg['Subject']='Toyota Feedback'
    msg['From']= sender_email
    msg['To'] = receiver_email

    # Send Email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendemail(sender_email, receiver_email, msg.as_string())
