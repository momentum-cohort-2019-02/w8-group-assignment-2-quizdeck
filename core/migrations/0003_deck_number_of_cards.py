# Generated by Django 2.2 on 2019-04-03 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190403_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='number_of_cards',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
