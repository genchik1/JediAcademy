# Generated by Django 3.0.7 on 2020-08-27 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0013_auto_20200827_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='jedi',
            name='count_padavans',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
