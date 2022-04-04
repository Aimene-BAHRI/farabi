# Generated by Django 3.2.6 on 2022-02-06 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20220202_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='activities',
        ),
        migrations.AddField(
            model_name='student',
            name='activities',
            field=models.ManyToManyField(blank=True, null=True, related_name='fils', to='home.Activity'),
        ),
    ]