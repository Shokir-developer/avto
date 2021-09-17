# Generated by Django 3.2.6 on 2021-09-07 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarsGM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('karobka', models.CharField(choices=[('avtomat', 'avtomat'), ('mexanika', 'maxanika')], max_length=50, null=True)),
                ('yili', models.DateField()),
                ('narxi', models.PositiveIntegerField()),
                ('mator', models.CharField(choices=[('1.6', '1.6'), ('1.8', '1.8'), ('2.0', '2.0'), ('2.2', '2.2'), ('2.4', '2.4')], max_length=20)),
                ('rang', models.CharField(choices=[('oq', 'oq'), ('qora', 'qora'), ('qizil', 'qizil'), ('sariq', 'sariq'), ('kulrang', 'kulrang')], max_length=20, null=True)),
                ('soni', models.PositiveIntegerField()),
            ],
        ),
    ]
