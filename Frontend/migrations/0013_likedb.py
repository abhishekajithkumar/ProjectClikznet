# Generated by Django 4.2.4 on 2023-11-09 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0012_remove_postdb_id_postdb_postid_postdb_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PostId', models.CharField(max_length=500)),
                ('UserId', models.CharField(max_length=100)),
            ],
        ),
    ]
