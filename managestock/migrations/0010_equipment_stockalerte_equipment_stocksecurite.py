# Generated by Django 4.1.7 on 2023-04-18 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managestock', '0009_discharge_datecreated'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='stockAlerte',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='equipment',
            name='stockSecurite',
            field=models.IntegerField(default=50),
        ),
    ]