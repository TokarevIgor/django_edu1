# Generated by Django 3.2.9 on 2021-12-15 17:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='city',
            field=models.CharField(blank=True, max_length=64, verbose_name='город'),
        ),
        migrations.AddField(
            model_name='shopuser',
            name='phone_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=14, verbose_name='номер телефона'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(blank=True, verbose_name='возраст'),
        ),
    ]
