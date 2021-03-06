# Generated by Django 3.1.7 on 2021-03-30 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestApi', '0003_auto_20210329_2348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Shows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('maturity_rating', models.CharField(max_length=3)),
                ('Language', models.CharField(max_length=16)),
                ('Country', models.CharField(max_length=16)),
                ('poster', models.URLField()),
                ('likes', models.IntegerField(default=0)),
                ('disLikes', models.IntegerField(default=0)),
                ('publishDate', models.DateField(blank=True, null=True)),
                ('views', models.IntegerField(default=0)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Actors', models.ManyToManyField(to='RestApi.Actors')),
                ('Categories', models.ManyToManyField(to='RestApi.Categories')),
            ],
        ),
    ]
