# Generated by Django 5.0.4 on 2024-04-17 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0004_alter_todo_done_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="done_date",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
