# Generated by Django 4.2.4 on 2023-11-27 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0024_commentdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='postdb',
            name='no_of_comments',
            field=models.IntegerField(default=0),
        ),
    ]
