# Generated by Django 3.2.5 on 2021-07-03 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=150)),
                ('courses', models.CharField(max_length=300)),
            ],
        ),
    ]