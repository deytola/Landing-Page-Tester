# Generated by Django 3.0.3 on 2020-06-09 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingPageTester', '0003_auto_20200609_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page_signups',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_traffic',
            field=models.FloatField(default=0),
        ),
    ]
