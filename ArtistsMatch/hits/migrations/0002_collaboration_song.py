# Generated by Django 3.2.9 on 2021-11-21 16:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaboration',
            name='song',
            field=models.FileField(default=django.utils.timezone.now, upload_to='hits/collaborations/'),
            preserve_default=False,
        ),
    ]
