# Generated by Django 5.0 on 2023-12-20 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_staffregister_loogin_credential_sent_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staffregister',
            old_name='loogin_credential_sent',
            new_name='login_credential_sent',
        ),
    ]
