# Generated by Django 4.0.5 on 2022-06-22 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmo', '0006_alter_compra_propiedad_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='contactado',
            field=models.BooleanField(null=True),
        ),
    ]
