# Generated by Django 3.2.13 on 2023-01-31 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_draft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='draft',
            field=models.BooleanField(default=True),
        ),
    ]
