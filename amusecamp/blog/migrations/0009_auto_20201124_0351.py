# Generated by Django 3.0.2 on 2020-11-24 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blog_post_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='snippet',
            field=models.CharField(default='Click Link above to Read More...', max_length=255),
        ),
    ]
