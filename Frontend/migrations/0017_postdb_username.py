# Generated by Django 4.2.4 on 2023-11-14 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0016_remove_postdb_username_commentdb_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='postdb',
            name='Username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]