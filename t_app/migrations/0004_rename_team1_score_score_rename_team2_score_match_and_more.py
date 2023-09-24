# Generated by Django 4.1.7 on 2023-09-23 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('t_app', '0003_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='team1',
            new_name='Score',
        ),
        migrations.RenameField(
            model_name='score',
            old_name='team2',
            new_name='match',
        ),
        migrations.RemoveField(
            model_name='score',
            name='team1_score',
        ),
        migrations.RemoveField(
            model_name='score',
            name='team2_score',
        ),
    ]
