# Generated by Django 4.2.3 on 2023-07-17 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0002_customer_date_created_customer_profile_pic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='tags',
            field=models.ManyToManyField(to='appstore.tag'),
        ),
    ]
