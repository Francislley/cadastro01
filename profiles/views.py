from django.shortcuts import render
from django.shortcuts import redirect
from profiles.models import Profile, Invite

def index(request):
  return render(request, 'index.html', { 'profiles': Profile.objects.all(), 'profile_logged_in': get_user_logged_in(request)})

def show(request, profile_id):
  profile = Profile()
  profile = Profile.objects.get(id = profile_id)

  return render(request, 'profile.html', { 'profile': profile, 'profile_logged_in': get_user_logged_in(request)})

def invite(request, profile_id):
  profile_to_invite = Profile.objects.get(id = profile_id)
  profile_logged_in = get_user_logged_in(request)
  profile_logged_in.invite(profile_to_invite)
  return redirect('index')

def accept(request, invite_id):
  invite = Invite.objects.get(id=invite_id)
  invite.accept()
  return redirect('index')

def get_user_logged_in(request):
  # Thiago always logged in, to test
  return Profile.objects.get(id = 1)