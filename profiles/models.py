from django.db import models

class Profile(models.Model):
  
  name = models.CharField(max_length = 255, null = False)
  email = models.CharField(max_length = 255, null = False)
  phone_number = models.CharField(max_length = 15, null = False)
  company_name = models.CharField(max_length = 255, null = False)

  def invite(self, profile_invited):
    invite = Invite(requester = self, invited = profile_invited)
    invite.save()

class Invite(models.Model):
  requester = models.ForeignKey(Profile, related_name = 'invitations_made')
  invited = models.ForeignKey(Profile, related_name = 'invitations_received')