# Generated by Django 4.0.1 on 2022-02-07 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0013_caraousel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='address',
        ),
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
