# Generated by Django 2.2 on 2019-05-22 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0004_userfileupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='coutner',
            field=models.IntegerField(default=1),
        ),
    ]
