# Generated by Django 5.1.3 on 2024-12-13 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder_app', '0009_review_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='features',
            field=models.JSONField(blank=True, default=list),
        ),
    ]