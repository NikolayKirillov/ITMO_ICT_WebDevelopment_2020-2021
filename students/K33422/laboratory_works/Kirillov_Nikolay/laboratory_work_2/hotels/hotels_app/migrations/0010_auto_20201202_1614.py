# Generated by Django 3.1.3 on 2020-12-02 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels_app', '0009_auto_20201202_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestsbase',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels_app.room', verbose_name='Room'),
        ),
    ]
