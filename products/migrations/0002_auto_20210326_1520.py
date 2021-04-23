# Generated by Django 3.1.7 on 2021-03-26 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]