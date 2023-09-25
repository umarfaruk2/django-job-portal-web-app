# Generated by Django 4.2.3 on 2023-09-24 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=70, unique=True)),
                ('about', models.TextField(max_length=150)),
                ('phone', models.CharField(max_length=20)),
                ('skill', models.CharField(choices=[('Javascript', 'Javascript'), ('React', 'React'), ('Django', 'Django'), ('Python', 'Python'), ('MySql', 'MySql'), ('HTML', 'HTML'), ('CSS', 'CSS')], max_length=20)),
                ('jobPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.jobpostmodel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.registerinfomodel')),
            ],
        ),
    ]
