# Generated by Django 5.1.3 on 2024-12-05 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0003_alter_books_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('info', models.TextField()),
            ],
        ),
    ]
