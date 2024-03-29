# Generated by Django 4.2.4 on 2023-11-14 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0014_postdb_no_of_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PostId', models.CharField(max_length=500)),
                ('UserId', models.CharField(max_length=100)),
                ('Comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='postdb',
            name='PImage',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='PostImage'),
        ),
    ]
