# Generated by Django 3.2.7 on 2021-10-18 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211018_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='group',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
