# Generated by Django 4.0.2 on 2022-06-26 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='age',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='worker',
            name='exp',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='worker',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
