# Generated by Django 3.0.7 on 2020-08-26 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0008_auto_20200826_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jedi',
            name='grade',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='academy.Grade'),
        ),
    ]