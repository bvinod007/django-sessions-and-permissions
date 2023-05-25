# Generated by Django 4.2.1 on 2023-05-25 07:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_author',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='uuid',
            field=models.UUIDField(auto_created=True, primary_key=True, serialize=False, unique=uuid.UUID('09b37c8e-5d1f-4027-9e12-b99620972e93')),
        ),
    ]