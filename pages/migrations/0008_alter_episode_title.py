# Generated by Django 3.2.5 on 2021-10-12 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_episode_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='title',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
