# Generated by Django 4.0.2 on 2022-07-04 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_post_alter_worker_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='photo',
            field=models.ImageField(default='cat.jpg', upload_to='photo/'),
        ),
    ]