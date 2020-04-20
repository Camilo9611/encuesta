# Generated by Django 3.0.3 on 2020-04-12 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200411_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregservicio',
            name='agilidad',
            field=models.IntegerField(choices=[('5', 'Excelente'), ('4', 'Bueno'), ('3', 'Regular'), ('2', 'Deficiente'), ('1', 'Malo')], default='5', help_text='Seleccione una opccion'),
        ),
        migrations.AlterField(
            model_name='pregservicio',
            name='ambientacion',
            field=models.IntegerField(choices=[('5', 'Excelente'), ('4', 'Bueno'), ('3', 'Regular'), ('2', 'Deficiente'), ('1', 'Malo')], default='5', help_text='Seleccione una opccion'),
        ),
        migrations.AlterField(
            model_name='pregservicio',
            name='calidad',
            field=models.IntegerField(choices=[('5', 'Excelente'), ('4', 'Bueno'), ('3', 'Regular'), ('2', 'Deficiente'), ('1', 'Malo')], default='5', help_text='Seleccione una opccion'),
        ),
        migrations.AlterField(
            model_name='pregservicio',
            name='eficiencia',
            field=models.IntegerField(choices=[('5', 'Excelente'), ('4', 'Bueno'), ('3', 'Regular'), ('2', 'Deficiente'), ('1', 'Malo')], default='5', help_text='Seleccione una opccion'),
        ),
        migrations.AlterField(
            model_name='pregservicio',
            name='presentacion',
            field=models.IntegerField(choices=[('5', 'Excelente'), ('4', 'Bueno'), ('3', 'Regular'), ('2', 'Deficiente'), ('1', 'Malo')], default='5', help_text='Seleccione una opccion'),
        ),
        migrations.AlterField(
            model_name='pregservicio',
            name='sabor',
            field=models.IntegerField(choices=[('5', 'Excelente'), ('4', 'Bueno'), ('3', 'Regular'), ('2', 'Deficiente'), ('1', 'Malo')], default='5', help_text='Seleccione una opccion'),
        ),
        migrations.AlterField(
            model_name='pregservicio',
            name='temperatura',
            field=models.IntegerField(choices=[('5', 'Excelente'), ('4', 'Bueno'), ('3', 'Regular'), ('2', 'Deficiente'), ('1', 'Malo')], default='5', help_text='Seleccione una opccion'),
        ),
    ]
