# Generated by Django 4.0.2 on 2022-06-26 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='worker',
            fields=[
                ('id', models.UUIDField(help_text='ID', primary_key=True, serialize=False)),
                ('FIO', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('exp', models.IntegerField()),
                ('Departament', models.CharField(help_text='Отдел', max_length=70)),
            ],
        ),
    ]