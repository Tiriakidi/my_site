# Generated by Django 2.2.6 on 2021-04-20 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0004_auto_20210408_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Book')),
            ],
        ),
    ]
