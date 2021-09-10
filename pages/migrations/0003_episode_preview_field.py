# Generated by Django 3.2.5 on 2021-08-03 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210730_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='preview',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='episode',
            name='theme',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='episode',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
