# Generated by Django 4.1.7 on 2023-07-21 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_client_rent'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='valor_aluguel',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Valor do aluguel'),
        ),
    ]
