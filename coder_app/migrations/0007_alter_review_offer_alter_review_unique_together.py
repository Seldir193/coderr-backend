# Generated by Django 5.1.3 on 2024-12-09 22:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder_app', '0006_review_offer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offer_reviews', to='coder_app.offer'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('business_user', 'reviewer', 'offer')},
        ),
    ]