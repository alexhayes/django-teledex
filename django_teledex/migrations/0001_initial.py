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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('kind', models.CharField(help_text='The kind of address.', db_index=True, default='postal', choices=[('postal', 'postal'), ('physical', 'physical')], max_length=16, verbose_name='kind')),
                ('status', models.CharField(help_text='Defines the current status of the address.', db_index=True, default='active', choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=16, verbose_name='status')),
                ('recipient', models.CharField(blank=True, null=True, help_text='Recipient', verbose_name='recipient', max_length=255)),
                ('organisation', models.CharField(blank=True, null=True, help_text='Organisation', verbose_name='organisation', max_length=255)),
                ('address_line', models.CharField(null=True, help_text='Street address lines separated by commas (,)', verbose_name='address', max_length=255)),
                ('locality', models.CharField(null=True, help_text='City or town', verbose_name='locality', max_length=255)),
                ('region', models.CharField(null=True, help_text='State code, country or canton', verbose_name='region', max_length=128)),
                ('postcode', models.CharField(null=True, help_text='Postal code, post code ZIP code', verbose_name='postcode', max_length=32)),
                ('country', django_countries.fields.CountryField(null=True, verbose_name='country', max_length=2, db_index=True)),
                ('owner_id', models.PositiveIntegerField(blank=True, null=True, db_index=True)),
                ('owner_type', models.ForeignKey(blank=True, null=True, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('kind', models.CharField(help_text='The kind of email.', db_index=True, default='work', choices=[('work', 'work'), ('home', 'home')], max_length=16, verbose_name='kind')),
                ('status', models.CharField(help_text='Defines the current status of the email.', db_index=True, default='active', choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=16, verbose_name='status')),
                ('email', models.EmailField(db_index=True, max_length=191)),
                ('owner_id', models.PositiveIntegerField(blank=True, null=True, db_index=True)),
                ('owner_type', models.ForeignKey(blank=True, null=True, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('kind', models.CharField(help_text='The kind of phone number.', db_index=True, default='work', choices=[('mobile', 'mobile'), ('work', 'work'), ('home', 'home'), ('main', 'main'), ('workfax', 'workfax'), ('homefax', 'homefax'), ('googlevoice', 'googlevoice'), ('pager', 'pager')], max_length=16, verbose_name='kind')),
                ('status', models.CharField(help_text='Defines the current status of the phone number.', db_index=True, default='active', choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=16, verbose_name='status')),
                ('number', phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=40)),
                ('owner_id', models.PositiveIntegerField(blank=True, null=True, db_index=True)),
                ('owner_type', models.ForeignKey(blank=True, null=True, to='contenttypes.ContentType')),
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
