from django.conf import settings
import random
import string
from datetime import date
import datetime


def generate_client_token():
    return gateway.client_token.generate()