# Generated by Django 4.2.5 on 2023-09-14 02:09

import ckeditor.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('title', models.CharField(max_length=128, verbose_name='Brand title')),
                ('description', models.TextField(verbose_name='Brand description')),
                ('logo', models.ImageField(upload_to='images/brands/%Y/%m/', verbose_name='Brand logo')),
                ('is_new', models.BooleanField(default=True, verbose_name='New status')),
                ('is_popular', models.BooleanField(default=False, verbose_name='Popular status')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('title', models.CharField(max_length=128, verbose_name='Category title')),
                ('icon', models.ImageField(upload_to='images/store/categories/icons', verbose_name='Category icon')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('title', models.CharField(max_length=256, verbose_name='Collection title')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description')),
                ('photo', models.ImageField(upload_to='images/collections/%Y/%m/', verbose_name='Collection photo')),
            ],
            options={
                'verbose_name': 'Collection',
                'verbose_name_plural': 'Collections',
            },
        ),
        migrations.CreateModel(
            name='SkinType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Skin type title')),
            ],
            options={
                'verbose_name': 'Skin type',
                'verbose_name_plural': 'Skin types',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('vendor_code', models.PositiveIntegerField(unique=True, verbose_name='Vendor code')),
                ('title', models.CharField(max_length=256, verbose_name='Product title')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Product description')),
                ('application', ckeditor.fields.RichTextField(verbose_name='Application')),
                ('ingredients', models.TextField(verbose_name='Ingredients')),
                ('price', models.PositiveIntegerField(verbose_name='Product price')),
                ('discount', models.PositiveIntegerField(default=0, verbose_name='Discount')),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Product rating')),
                ('purchase_count', models.PositiveIntegerField(default=0, verbose_name='Purchase count')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Views count')),
                ('is_new', models.BooleanField(default=True, verbose_name='New status')),
                ('is_hit', models.BooleanField(default=False, verbose_name='Hit status')),
                ('is_bestseller', models.BooleanField(default=False, verbose_name='Bestseller status')),
                ('is_tiktok', models.BooleanField(default=False, verbose_name='TikTok product status')),
                ('is_miniature', models.BooleanField(default=False, verbose_name='Miniature status')),
                ('popularity', models.DecimalField(decimal_places=2, default=0, max_digits=24, verbose_name='Popularity')),
                ('is_available', models.BooleanField(default=True, verbose_name='Available status')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='store.brand', verbose_name='Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='store.category', verbose_name='Category')),
                ('collections', models.ManyToManyField(blank=True, related_name='products', to='store.collection', verbose_name='Collections')),
                ('skin_types', models.ManyToManyField(blank=True, related_name='products', to='store.skintype', verbose_name='Suitable skin types')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/store/products/%Y/%m/', verbose_name='Photo')),
                ('ordinal_number', models.PositiveIntegerField(blank=True, null=True, verbose_name='Ordinal number')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='photos', to='store.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
                'ordering': ['ordinal_number'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos/store/products/%Y/%m/', verbose_name='Video')),
                ('ordinal_number', models.PositiveIntegerField(blank=True, null=True, verbose_name='Ordinal number')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='videos', to='store.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
                'ordering': ['ordinal_number'],
                'unique_together': {('product', 'ordinal_number')},
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5, message='Max allowed number is 5')], verbose_name='Rating')),
                ('review', models.CharField(blank=True, max_length=512, null=True, verbose_name='Review')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='store.product', verbose_name='Reviewed product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='Reviewer user')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
                'unique_together': {('user', 'product')},
            },
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['title'], name='store_produ_title_244706_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='photo',
            unique_together={('product', 'ordinal_number')},
        ),
    ]
