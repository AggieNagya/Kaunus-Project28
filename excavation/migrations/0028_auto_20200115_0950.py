# Generated by Django 2.2.9 on 2020-01-15 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excavation', '0027_auto_20200115_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='slug',
            field=models.SlugField(max_length=250, null=True, unique=True),
        ),
    ]
