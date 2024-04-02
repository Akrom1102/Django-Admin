# Generated by Django 5.0.3 on 2024-04-02 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_bookingbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('book', models.ManyToManyField(to='library.book')),
            ],
        ),
    ]
