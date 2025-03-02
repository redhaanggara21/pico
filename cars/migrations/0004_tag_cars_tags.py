# Generated by Django 5.1.2 on 2024-10-15 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_address_fixhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='cars',
            name='tags',
            field=models.ManyToManyField(to='cars.tag'),
        ),
    ]
