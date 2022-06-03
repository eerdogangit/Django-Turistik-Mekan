# Generated by Django 3.2 on 2022-06-03 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0007_alter_place_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='status',
            field=models.CharField(choices=[('New', 'Yeni'), ('True', 'Evet'), ('False', 'Hayır')], default='New', max_length=10),
        ),
    ]