# Generated by Django 3.0.3 on 2020-04-11 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregservicio',
            name='calidad',
            field=models.IntegerField(blank=True, choices=[('5', 'Excelente'), ('4', 'Bueno'), ('3', 'Regular'), ('2', 'Deficiente'), ('1', 'Malo')], help_text='Seleccione una opccion'),
        ),
    ]