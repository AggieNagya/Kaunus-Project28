# Generated by Django 2.2.9 on 2019-12-31 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('excavation', '0008_auto_20191231_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='find',
            name='area',
        ),
        migrations.RemoveField(
            model_name='find',
            name='finding',
        ),
        migrations.RemoveField(
            model_name='find',
            name='trench',
        ),
    ]
