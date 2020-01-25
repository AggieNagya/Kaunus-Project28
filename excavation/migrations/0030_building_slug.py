# Generated by Django 2.2.9 on 2020-01-15 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excavation', '0029_remove_building_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
