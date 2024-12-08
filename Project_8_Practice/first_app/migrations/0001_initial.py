# Generated by Django 5.1.3 on 2024-12-08 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('father_name', models.TextField(default='Anower')),
            ],
        ),
    ]
