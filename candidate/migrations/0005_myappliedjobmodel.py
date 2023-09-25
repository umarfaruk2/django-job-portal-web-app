# Generated by Django 4.2.3 on 2023-09-25 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('candidate', '0004_alter_candidatemodel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyAppliedJobModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidate.candidatemodel')),
                ('jobPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.jobpostmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]