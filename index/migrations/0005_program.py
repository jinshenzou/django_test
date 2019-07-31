# Generated by Django 2.2.1 on 2019-07-31 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_remove_product_name2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('performer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Performer')),
            ],
        ),
    ]
