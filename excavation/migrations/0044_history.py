# Generated by Django 2.2.9 on 2020-01-17 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excavation', '0043_topography'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editor', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
        ),
    ]
