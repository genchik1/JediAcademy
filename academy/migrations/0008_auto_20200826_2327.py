# Generated by Django 3.0.7 on 2020-08-26 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0007_auto_20200826_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jedi',
            name='grade',
            field=models.CharField(choices=[('grand-master', 'Grand-Master'), ('master', 'Master'), ('knight', 'Knight'), ('padawan', 'Padawan')], max_length=25),
        ),
    ]
