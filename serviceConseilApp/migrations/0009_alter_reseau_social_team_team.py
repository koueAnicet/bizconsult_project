# Generated by Django 4.0.5 on 2022-06-10 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serviceConseilApp', '0008_alter_reseau_social_team_icon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reseau_social_team',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userTeamSocial', to='serviceConseilApp.team'),
        ),
    ]
