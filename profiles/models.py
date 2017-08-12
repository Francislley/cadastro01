from django.db import models

class Profile(object):

  def __init__(self, name='', email='', phone_number='', company_name=''):
    self.name = name
    self.email = email
    self.phone_number = phone_number
    self.company_name = company_name