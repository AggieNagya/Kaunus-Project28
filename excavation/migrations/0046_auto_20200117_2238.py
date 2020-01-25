# Generated by Django 2.2.9 on 2020-01-17 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excavation', '0045_monument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='find',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='finding',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='monument',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='trench',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
