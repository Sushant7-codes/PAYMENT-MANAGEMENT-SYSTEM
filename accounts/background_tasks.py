from background_task import background
from django.core.mail import send_mail
from django.conf import settings
    
@background(schedule=2)
def send_otp(email,new_otp):  #background task
    subject = "Password Reset OTP"
    message=f'''
        Use the following OTP to reset your password: {new_otp}
        OR 
        Follow the link to reset the password: http://127.0.0.1:8000/accounts/set-new-password
    '''
    send_mail(subject, message,settings.EMAIL_HOST_USER, [email])
    
    
    print("Code sent successfully to", email)