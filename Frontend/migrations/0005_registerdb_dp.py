# Generated by Django 4.2.4 on 2023-10-29 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0004_remove_postdb_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerdb',
            name='DP',
            field=models.ImageField(default='default.jpg', upload_to='DP'),
        ),
    ]