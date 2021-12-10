# Generated by Django 4.0 on 2021-12-10 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=100)),
                ('page', models.IntegerField(default=0)),
                ('publication_date', models.DateField()),
                ('publisher', models.CharField(max_length=60)),
                ('author', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]