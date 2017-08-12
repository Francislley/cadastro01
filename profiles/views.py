from django.shortcuts import render
from profiles.models import Profile

def index(request):
  return render(request, 'index.html')

def show(request, profile_id):
  profile = Profile()

  if profile_id == '1':
    profile = Profile('Thiago Moreira', 'thiago@gmail.com', '999999999', 'Empresa')
    
  return render(request, 'profile.html')