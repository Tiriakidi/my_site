# Generated by Django 2.2.6 on 2021-04-30 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0007_auto_20210420_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='test',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='full_name',
            field=models.CharField(max_length=100),
        ),
    ]
