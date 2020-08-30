# Generated by Django 3.0.7 on 2020-08-30 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0015_сandidate_answered_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academy.Choice'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='candidate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academy.Сandidate'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='qestions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academy.Question'),
        ),
    ]
