# Generated by Django 2.1.5 on 2019-06-16 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_tags_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='name',
        ),
    ]
