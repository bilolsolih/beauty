# Generated by Django 4.2.5 on 2023-09-14 02:09

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, null=True, verbose_name='Title')),
                ('photo', models.ImageField(upload_to='images/banners/', verbose_name='Photo')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'AdBanner',
                'verbose_name_plural': 'AdBanners',
            },
        ),
        migrations.CreateModel(
            name='FQA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=512, verbose_name='Question')),
                ('answer', models.TextField(verbose_name='Answer')),
                ('type', models.CharField(choices=[('Delivery', 'Delivery'), ('General', 'General')], max_length=8, verbose_name='Question type')),
            ],
            options={
                'verbose_name': 'FQA',
                'verbose_name_plural': 'FQAs',
            },
        ),
        migrations.CreateModel(
            name='StaticText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('d', 'Delivery'), ('w', 'Warranty'), ('p', 'Payment'), ('h', 'Hiring prompt'), ('a', 'About company'), ('t', 'Terms and Conditions'), ('r', 'Requisites')], max_length=1, unique=True, verbose_name='Text type')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Static text',
                'verbose_name_plural': 'Static texts',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('title', models.CharField(max_length=256, verbose_name='Job title')),
                ('location', models.CharField(max_length=256, verbose_name='Location')),
                ('vacancies', models.PositiveIntegerField(blank=True, null=True, verbose_name='Number of vacant positions')),
            ],
            options={
                'verbose_name': 'Vacancy',
                'verbose_name_plural': 'Vacancies',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('full_name', models.CharField(max_length=128, verbose_name='Full name')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('resume', models.FileField(upload_to='files/resumes/%Y/%m/', verbose_name='Resume file')),
                ('text_resume', models.TextField(verbose_name='Text resume')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to='about.vacancy', verbose_name='Vacancy')),
            ],
            options={
                'verbose_name': 'Resume',
                'verbose_name_plural': 'Resumes',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=128, verbose_name='Full name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone number')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'unique_together': {('email', 'phone_number')},
            },
        ),
    ]
