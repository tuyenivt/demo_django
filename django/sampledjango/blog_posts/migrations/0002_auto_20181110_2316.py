# Generated by Django 2.0.9 on 2018-11-10 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_posts',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog_posts',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog_posts',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
