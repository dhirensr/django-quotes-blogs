# Generated by Django 4.1.5 on 2023-01-24 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_links', models.CharField(max_length=800)),
            ],
        ),
        migrations.RemoveField(
            model_name='quotes',
            name='added_date',
        ),
    ]
