# Generated by Django 2.2.13 on 2020-06-16 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_performance_satisfaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='distance_run',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=4),
        ),
    ]
