# Generated by Django 3.2.23 on 2024-02-10 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0005_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='job_number',
            field=models.CharField(max_length=50, null=True, verbose_name='job number'),
        ),
    ]
