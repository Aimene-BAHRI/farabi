# Generated by Django 3.2.6 on 2022-01-25 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220125_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='study_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fils', to='home.studylevel'),
        ),
    ]
