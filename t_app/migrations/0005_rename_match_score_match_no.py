# Generated by Django 4.1.7 on 2023-09-24 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('t_app', '0004_rename_team1_score_score_rename_team2_score_match_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='match',
            new_name='match_no',
        ),
    ]