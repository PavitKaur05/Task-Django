# Generated by Django 3.0.3 on 2020-04-14 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task_django', '0002_auto_20200414_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]