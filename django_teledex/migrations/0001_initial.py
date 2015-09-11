# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.CharField(default='postal', max_length=16, db_index=True, choices=[('postal', 'postal'), ('physical', 'physical')], verbose_name='kind', help_text='The kind of address')),
                ('status', models.CharField(default='active', max_length=16, db_index=True, choices=[('active', 'active'), ('inactive', 'inactive')], verbose_name='status', help_text='Defines the current status of the address')),
                ('recipient', models.CharField(verbose_name='recipient', blank=True, help_text='Recipient', max_length=255, null=True)),
                ('organisation', models.CharField(verbose_name='organisation', blank=True, help_text='Organisation', max_length=255, null=True)),
                ('address_line', models.CharField(verbose_name='address', help_text='Street address lines separated by commas (,)', max_length=255, null=True)),
                ('locality', models.CharField(verbose_name='locality', help_text='City or town', max_length=255, null=True)),
                ('region', models.CharField(verbose_name='region', help_text='State code, country or canton', max_length=128, null=True)),
                ('postcode', models.CharField(verbose_name='postcode', help_text='Postal code, post code ZIP code', max_length=32, null=True)),
                ('country', django_countries.fields.CountryField(verbose_name='country', db_index=True, max_length=2, null=True)),
                ('owner_id', models.PositiveIntegerField(blank=True, db_index=True, null=True)),
                ('owner_type', models.ForeignKey(to='contenttypes.ContentType', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.CharField(default='work', max_length=16, db_index=True, choices=[('work', 'work'), ('home', 'home')], verbose_name='kind', help_text='The kind of email')),
                ('status', models.CharField(default='active', max_length=16, db_index=True, choices=[('active', 'active'), ('inactive', 'inactive')], verbose_name='status', help_text='Defines the current status of the email')),
                ('email', models.EmailField(db_index=True, max_length=191)),
                ('owner_id', models.PositiveIntegerField(blank=True, db_index=True, null=True)),
                ('owner_type', models.ForeignKey(to='contenttypes.ContentType', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.CharField(default='work', max_length=16, db_index=True, choices=[('mobile', 'mobile'), ('work', 'work'), ('home', 'home'), ('main', 'main'), ('workfax', 'work fax'), ('homefax', 'home fax'), ('googlevoice', 'google voice'), ('pager', 'pager')], verbose_name='kind', help_text='The kind of phone number')),
                ('status', models.CharField(default='active', max_length=16, db_index=True, choices=[('active', 'active'), ('inactive', 'inactive')], verbose_name='status', help_text='Defines the current status of the phone number')),
                ('number', phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=40)),
                ('owner_id', models.PositiveIntegerField(blank=True, db_index=True, null=True)),
                ('owner_type', models.ForeignKey(to='contenttypes.ContentType', blank=True, null=True)),
            ],
        ),
        migrations.AlterIndexTogether(
            name='phonenumber',
            index_together=set([('owner_type', 'owner_id')]),
        ),
        migrations.AlterIndexTogether(
            name='email',
            index_together=set([('owner_type', 'owner_id')]),
        ),
        migrations.AlterIndexTogether(
            name='address',
            index_together=set([('owner_type', 'owner_id')]),
        ),
    ]
