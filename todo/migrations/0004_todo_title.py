# Generated by Django 4.0.4 on 2022-05-18 10:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_todo_title_todo_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]