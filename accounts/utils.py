from .background_tasks import send_otp

def is_email_valid(email):
    if email is not None and email != " " and email != "" and "@" not in email and "." not in email:
        return False
    
    return True



def forgot_password_email(email):
    from .models import OTP
    
    
    try:
        new_otp=OTP.generate_otp(email)
        
    except Exception as e:
        raise Exception(str(e))
    
    send_otp(email,new_otp)
    
def password_changed_email(email):
    from django.core.mail import send_mail
    from django.conf import settings
    
    subject = "Password Changed Successfully"
    message='''
        Your password has been changed successfully.
        Now you can login with your new password.
        If you did not make this change, please contact support.
    '''
    send_mail(subject, message,settings.EMAIL_HOST_USER, [email])
