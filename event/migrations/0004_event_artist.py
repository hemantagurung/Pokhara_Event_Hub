# Generated by Django 5.1.6 on 2025-03-30 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_remove_event_description_event_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='artist',
            field=models.CharField(default='Prabin', max_length=255),
        ),
    ]
