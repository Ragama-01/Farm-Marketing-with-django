# Generated by Django 4.2.7 on 2023-11-29 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0008_blog_color_cart_color_customer_color_farmer_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Category',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
