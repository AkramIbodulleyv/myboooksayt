# Generated by Django 5.1.3 on 2024-12-06 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0004_buy'),
    ]

    operations = [
        migrations.CreateModel(
            name='foydalanuvchimalumoti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=100)),
                ('birth_date', models.DateField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Buy',
        ),
    ]