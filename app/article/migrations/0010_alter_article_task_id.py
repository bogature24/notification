# Generated by Django 3.2.3 on 2023-02-02 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_auto_20230202_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='task_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
