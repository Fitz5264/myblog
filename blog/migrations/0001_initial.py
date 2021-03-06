# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-02 12:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='authInformation',
            fields=[
                ('avatar', models.ImageField(upload_to='blog/images/%Y_%m_%d/')),
                ('introduction', models.CharField(max_length=800)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birthday', models.DateTimeField()),
                ('constellation', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('words', models.CharField(max_length=200)),
                ('addDate', models.DateTimeField(auto_now_add=True)),
                ('support_num', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-addDate'],
            },
        ),
        migrations.CreateModel(
            name='diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('introduction', models.CharField(default='', max_length=200)),
                ('writeDate', models.DateTimeField(auto_now_add=True)),
                ('modifyDate', models.DateTimeField(auto_now=True)),
                ('words', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comments', models.ManyToManyField(blank=True, to='blog.comment')),
            ],
            options={
                'ordering': ['-writeDate'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='essays/%Y_%m_%d/')),
                ('addDate', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-addDate'],
            },
        ),
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='blog/images/%Y_%m_%d/')),
                ('addDate', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-addDate'],
            },
        ),
        migrations.CreateModel(
            name='label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('addDate', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-addDate'],
            },
        ),
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction', models.CharField(max_length=50)),
                ('addDate', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('images', models.ManyToManyField(to='blog.image')),
            ],
            options={
                'ordering': ['-addDate'],
            },
        ),
        migrations.CreateModel(
            name='tech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('introduction', models.CharField(default='', max_length=200)),
                ('writeDate', models.DateTimeField(auto_now_add=True)),
                ('modifyDate', models.DateTimeField(auto_now=True)),
                ('words', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comments', models.ManyToManyField(blank=True, to='blog.comment')),
                ('files', models.ManyToManyField(blank=True, to='blog.file')),
                ('images', models.ManyToManyField(blank=True, to='blog.image')),
                ('labels', models.ManyToManyField(blank=True, to='blog.label')),
            ],
            options={
                'ordering': ['-writeDate'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('introduction', models.CharField(default='', max_length=200)),
                ('writeDate', models.DateTimeField(auto_now_add=True)),
                ('modifyDate', models.DateTimeField(auto_now=True)),
                ('words', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comments', models.ManyToManyField(blank=True, to='blog.comment')),
                ('files', models.ManyToManyField(blank=True, to='blog.file')),
                ('images', models.ManyToManyField(blank=True, to='blog.image')),
                ('labels', models.ManyToManyField(blank=True, to='blog.label')),
            ],
            options={
                'ordering': ['-writeDate'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='diary',
            name='files',
            field=models.ManyToManyField(blank=True, to='blog.file'),
        ),
        migrations.AddField(
            model_name='diary',
            name='images',
            field=models.ManyToManyField(blank=True, to='blog.image'),
        ),
        migrations.AddField(
            model_name='diary',
            name='labels',
            field=models.ManyToManyField(blank=True, to='blog.label'),
        ),
        migrations.AddField(
            model_name='authinformation',
            name='labels',
            field=models.ManyToManyField(blank=True, to='blog.label'),
        ),
    ]
