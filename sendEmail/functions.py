from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template
from django.contrib.auth.models import User

def send_mail(user_email, user, subjectI_line, content, html_content_text, template):
    

    subject, from_email, to = subjectI_line, settings.EMAIL_HOST_USER, user.email
    text_content = content
    html_content = ('<p>{}.</p>'.format(html_content_text))
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [user.email])
    html_template = get_template(template).render()
    msg.attach_alternative(html_template, "text/html")
    msg.send()