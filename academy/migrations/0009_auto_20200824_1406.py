# Generated by Django 3.1 on 2020-08-24 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0008_remove_сandidate_qestions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='choice',
            new_name='answer',
        ),
    ]
