# Generated by Django 4.0.3 on 2022-04-17 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='social_youtupe',
            new_name='social_stackoverflow',
        ),
    ]
