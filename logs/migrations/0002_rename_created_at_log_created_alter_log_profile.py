# Generated by Django 5.1.2 on 2024-10-15 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
        ('profiles', '0002_profile_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='created_at',
            new_name='created',
        ),
        migrations.AlterField(
            model_name='log',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]
