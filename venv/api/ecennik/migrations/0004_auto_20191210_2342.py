# Generated by Django 2.0.13 on 2019-12-10 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecennik', '0003_auto_20191210_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='towary',
            name='waga',
        ),
        migrations.AlterField(
            model_name='towary',
            name='cena',
            field=models.CharField(max_length=60),
        ),
    ]
