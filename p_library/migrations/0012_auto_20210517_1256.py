# Generated by Django 2.2.6 on 2021-05-17 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0011_auto_20210512_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='publisher',
            name='city',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='publisher',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='publisher',
            name='state_province',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='publisher',
            name='website',
            field=models.URLField(null=True),
        ),
    ]
