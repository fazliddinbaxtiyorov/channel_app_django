# Generated by Django 4.0.3 on 2023-08-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0002_alter_channel_post_content_alter_channel_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='post_content',
            field=models.TextField(max_length=440),
        ),
    ]
