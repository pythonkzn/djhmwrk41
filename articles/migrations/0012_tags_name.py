# Generated by Django 2.1.5 on 2019-06-16 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='name',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]