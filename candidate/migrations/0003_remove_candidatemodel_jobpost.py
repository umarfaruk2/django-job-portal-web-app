# Generated by Django 4.2.3 on 2023-09-24 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0002_remove_candidatemodel_skill_candidatemodel_education'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidatemodel',
            name='jobPost',
        ),
    ]
