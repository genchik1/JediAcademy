# Generated by Django 3.0.7 on 2020-08-31 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0021_jedi_count_padavans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='сandidate',
            name='jedi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='jed', to='academy.Jedi'),
        ),
    ]