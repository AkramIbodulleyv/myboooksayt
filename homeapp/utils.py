from django.core.mail import send_mail
from random import randint

def generate_verification_code():
    return str(random.randint(10000, 99999))



def send_verification_email(email,code):
    subject = "Tizimga Kirish uchun Kod"
    message = f"Sizning Tasdiqlash Kodingiz: {code}"
    from_email = 'EMAIL_HOST_USER'
    send_mail(subject, message, from_email, [email])
    return code



def save_verification_code(request):
    code = generate_verification_code()
    VerificationCode.objects.update_or_create(email=email, defaults={'code': code})
    return code

