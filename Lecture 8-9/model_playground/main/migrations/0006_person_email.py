# Generated by Django 2.0.7 on 2018-07-15 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20180715_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
