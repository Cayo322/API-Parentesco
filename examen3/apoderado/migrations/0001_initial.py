# Generated by Django 4.2.2 on 2023-06-18 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apoderado',
            fields=[
                ('apoderado_id', models.AutoField(primary_key=True, serialize=False)),
                ('apoderado_nombre', models.CharField(max_length=255)),
                ('apoderado_apellido', models.CharField(max_length=255)),
                ('apoderado_telefono', models.CharField(max_length=255)),
                ('apoderado_documento_identidad', models.CharField(max_length=20)),
                ('parentesco_id', models.IntegerField()),
            ],
        ),
    ]
