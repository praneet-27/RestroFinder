# Generated by Django 2.1.7 on 2019-03-25 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourpackage', '0002_remove_comments_comment_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='rating',
            new_name='rank',
        ),
    ]
