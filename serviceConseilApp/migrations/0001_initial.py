# Generated by Django 4.0.5 on 2022-06-09 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reseau_social_team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_team', models.URLField(null=True)),
                ('twitter_team', models.URLField(null=True)),
                ('linkedin_team', models.URLField(null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_service', models.CharField(max_length=255)),
                ('icon_service', models.CharField(max_length=30)),
                ('title_service', models.CharField(max_length=30)),
                ('description_service', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_team', models.CharField(max_length=100)),
                ('name_team', models.CharField(max_length=50)),
                ('job_team', models.CharField(max_length=100)),
                ('image_team', models.FileField(upload_to='img_team')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('reseau_social', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceConseilApp.reseau_social_team')),
            ],
        ),
    ]
