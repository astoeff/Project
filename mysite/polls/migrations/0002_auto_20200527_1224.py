# Generated by Django 3.0.6 on 2020-05-27 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='price',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Category'),
        ),
    ]
