# Generated by Django 4.2.1 on 2023-06-05 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_message_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='linkedin',
            new_name='whatsapp',
        ),
    ]
