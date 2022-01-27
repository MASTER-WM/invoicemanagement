from django.core.mail import EmailMessage
from django.conf import settings



def emailInvoiceClient(to_email, from_client, filepath):
    from_email = settings.EMAIL_HOST_USER
    subject = 'سفارش'
    body = """
باسلام و روز بخیر                                                       
    لطفا فایل ثبت سفارش خود را که در این ایمیل بارگزاری شده است چک کنین

    با احترام
    شرکت هیدرو صنعت پارسیان
    
    """.format(from_client)

    message = EmailMessage(subject, body, from_email, [to_email])
    message.attach_file(filepath)
    message.send()
