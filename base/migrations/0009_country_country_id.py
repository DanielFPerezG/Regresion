# Generated by Django 4.0.6 on 2022-12-19 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_varmodel_final_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='country_id',
            field=models.CharField(max_length=300, null=True),
        ),
    ]