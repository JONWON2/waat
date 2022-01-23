# Generated by Django 4.0.1 on 2022-01-22 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FundingBoard',
            fields=[
                ('board_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=30, null=True)),
                ('title', models.CharField(max_length=30, null=True)),
                ('content', models.TextField(null=True)),
                ('fund_goal_price', models.IntegerField()),
                ('fund_total_price', models.IntegerField()),
                ('regi_date', models.DateField()),
            ],
            options={
                'db_table': 'FundingBoard',
                'managed': False,
            },
        ),
    ]