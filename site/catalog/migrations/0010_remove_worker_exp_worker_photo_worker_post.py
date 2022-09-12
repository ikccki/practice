# Generated by Django 4.0.2 on 2022-07-04 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_product_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='exp',
        ),
        migrations.AddField(
            model_name='worker',
            name='photo',
            field=models.ImageField(default='cat.jpeg', upload_to='photo/'),
        ),
        migrations.AddField(
            model_name='worker',
            name='post',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
