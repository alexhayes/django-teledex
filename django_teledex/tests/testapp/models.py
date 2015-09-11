from django.db import models
from django_teledex.fields import AddressRelation, PhoneNumberRelation, \
    EmailRelation


class BaseModel(models.Model):

    def __unicode__(self):
        return u'%s' % self.pk


class ModelWithAddresses(BaseModel):
    addresses = AddressRelation('modelwithaddresses')


class ModelWithPhoneNumbers(BaseModel):
    phonenumbers = PhoneNumberRelation('modelwithphonenumbers')


class ModelWithEmails(BaseModel):
    emails = EmailRelation('modelwithemails')
