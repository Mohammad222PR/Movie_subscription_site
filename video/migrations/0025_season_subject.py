# Generated by Django 4.2.2 on 2023-07-29 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0024_remove_serial_season_season_season'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='subject',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='موضوع فصل'),
        ),
    ]
