# Generated by Django 4.1.7 on 2023-09-24 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t_app', '0005_rename_match_score_match_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='match_no',
            field=models.IntegerField(),
        ),
    ]
