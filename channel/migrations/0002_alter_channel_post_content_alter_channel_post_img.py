# Generated by Django 4.0.3 on 2023-08-15 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='post_content',
            field=models.TextField(max_length=240),
        ),
        migrations.AlterField(
            model_name='channel',
            name='post_img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
