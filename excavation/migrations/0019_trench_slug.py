# Generated by Django 2.2.9 on 2020-01-07 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excavation', '0018_auto_20191231_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='trench',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
