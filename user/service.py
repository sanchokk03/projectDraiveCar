from django.core.mail import send_mail
from random import randint


def generate_code():
    return randint(1000, 9999)


def send_reset_email(email, code):
    subject = "Сброс пароля"
    message = f"Ваш код сброса пароля: {code}"
    send_mail(subject, message, "isenbekovsanat8@gmail.com", [email])