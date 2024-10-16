# Generated by Django 5.1.2 on 2024-10-16 03:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('completed', models.BooleanField(default=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('category', models.IntegerField(choices=[(1, 'inbox'), (2, 'next'), (3, 'maybe'), (4, 'project')], default=1)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='projects.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=25)),
                ('color', models.CharField(default='424244', max_length=6)),
                ('tasks', models.ManyToManyField(blank=True, to='task.task')),
            ],
        ),
    ]
