# Generated by Django 3.2.4 on 2022-02-24 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loandata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loanDate', models.DateField()),
                ('releaseDate', models.DateField()),
                ('PrincipalAmount', models.IntegerField()),
            ],
        ),
    ]