# Generated by Django 3.1.3 on 2020-11-08 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_auth', '0002_auto_20201108_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uniformsuser',
            name='form_id',
            field=models.UUIDField(default=None, null=True, verbose_name='ID формы'),
        ),
    ]
