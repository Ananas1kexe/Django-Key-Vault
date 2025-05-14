import secrets
import os

from cryptography.fernet import Fernet
from .models import User, password
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password

from django_ratelimit.decorators import ratelimit


KEY_PATH = os.path.join(settings.BASE_DIR, ".env")

if not os.path.exists(KEY_PATH):
    with open(KEY_PATH, "wb") as f:
        f.write(Fernet.generate_key())

with open(KEY_PATH, "rb") as f:
    fernet = Fernet(f.read())
    
def encrypt_data(data: str) -> str:
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(token: str) -> str:
    return fernet.decrypt(token.encode()).decode()
# Create your views here.



def index(request):
    return render(request, "index.html")