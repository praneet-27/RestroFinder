# Generated by Django 2.1.7 on 2019-03-25 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourpackage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comment_no',
        ),
    ]
