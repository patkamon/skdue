# Generated by Django 3.2.8 on 2021-11-10 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skdue_calendar', '0007_calendartag_tag_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendartag',
            name='tag_color',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
