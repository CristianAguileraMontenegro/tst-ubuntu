# Generated by Django 4.1.2 on 2022-11-24 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.TextField(blank=True, null=True),
        ),
    ]