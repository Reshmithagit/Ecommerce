# Generated by Django 4.2.3 on 2023-08-11 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ca', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Addproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('price', models.IntegerField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('add', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecomapp.category')),
            ],
        ),
    ]
