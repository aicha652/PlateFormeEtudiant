# Generated by Django 2.2.8 on 2020-04-27 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200427_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='description',
            field=models.TextField(),
        ),
    ]