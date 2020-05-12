# Generated by Django 3.0.5 on 2020-05-09 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allaboutfeet', '0004_productdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('user_id', models.IntegerField()),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pid', models.IntegerField()),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('size', models.IntegerField()),
            ],
            options={
                'db_table': 'allaboutfeet_orders',
                'managed': False,
            },
        ),
    ]
