# Generated by Django 3.2.5 on 2022-04-25 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=155, null=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Product Category',
                'verbose_name_plural': 'Product Categories',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=155, null=True)),
            ],
            options={
                'verbose_name': 'Product Tag',
                'verbose_name_plural': 'Product Tags',
            },
        ),
        migrations.CreateModel(
            name='RestaurantCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=155, null=True)),
            ],
            options={
                'verbose_name': 'Restaurant Category',
                'verbose_name_plural': 'Restaurant Categories',
            },
        ),
        migrations.CreateModel(
            name='RestaurantType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=155, null=True)),
            ],
            options={
                'verbose_name': 'Restaurant Type',
                'verbose_name_plural': 'Restaurant Types',
            },
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=155, null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
                ('category_rest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.restaurantcategory')),
                ('type_rest', models.ManyToManyField(to='my_app.RestaurantType')),
            ],
            options={
                'verbose_name': 'Restaurant',
                'verbose_name_plural': 'Restaurants',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=155, null=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=300)),
                ('slug', models.SlugField(default=None, max_length=250, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.productcategory')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.restaurants')),
                ('tag', models.ManyToManyField(to='my_app.ProductTag')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['-created_at'],
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='my_app.cart')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='my_app.products')),
            ],
        ),
    ]
