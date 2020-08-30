# Generated by Django 3.0.7 on 2020-08-30 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0016_auto_20200830_1725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='ans',
        ),
        migrations.AddField(
            model_name='answer',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='academy.Answer', verbose_name='Родитель'),
        ),
    ]
