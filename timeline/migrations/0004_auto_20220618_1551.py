# Generated by Django 3.2.5 on 2022-06-18 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0003_alter_event_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='drive',
        ),
        migrations.AddField(
            model_name='event',
            name='Travel',
            field=models.BooleanField(default=False, help_text='Check if this is a drive or flight'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(blank=True, help_text='Description of the event (Optional)', max_length=600),
        ),
    ]
