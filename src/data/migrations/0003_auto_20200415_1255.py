# Generated by Django 3.0.5 on 2020-04-15 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20200415_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.IntegerField(choices=[(1, 'Uníca'), (2, 'Selección multiple'), (3, 'Numerica'), (4, 'Texto')], default=1, verbose_name='Tipo'),
        ),
    ]
