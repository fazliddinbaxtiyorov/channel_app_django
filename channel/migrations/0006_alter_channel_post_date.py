# Generated by Django 4.0.3 on 2023-08-15 11:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0005_alter_channel_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='post_date',
            field=models.DateTimeField(default=datetime.timezone),
        ),
    ]
