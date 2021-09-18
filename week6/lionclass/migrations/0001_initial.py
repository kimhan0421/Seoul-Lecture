# Generated by Django 3.2.7 on 2021-09-18 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LionClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail_image', models.CharField(blank=True, max_length=255)),
                ('status', models.CharField(choices=[(1, '모집'), (2, '마감')], max_length=2)),
                ('title', models.CharField(max_length=100)),
                ('title_description', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
