# Generated by Django 3.0.3 on 2020-04-13 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20200413_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregservicio',
            name='nroencuesta',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.Usuario'),
        ),
    ]
