# Generated by Django 3.1.7 on 2021-03-01 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='description',
            field=models.TextField(max_length=1024, null=True),
        ),
    ]