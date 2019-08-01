# Generated by Django 2.2.1 on 2019-07-31 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=20)),
                ('masterpiece', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Performer_info',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('birth', models.CharField(max_length=20)),
                ('elapse', models.CharField(max_length=20)),
                ('performer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='index.Performer')),
            ],
        ),
    ]