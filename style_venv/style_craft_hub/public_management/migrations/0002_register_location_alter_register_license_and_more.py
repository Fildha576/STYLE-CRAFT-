# Generated by Django 5.0.2 on 2024-03-16 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='location',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='license',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='usertype',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
