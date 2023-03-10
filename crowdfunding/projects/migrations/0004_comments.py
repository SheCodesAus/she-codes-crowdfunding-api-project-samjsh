# Generated by Django 4.1.5 on 2023-01-24 05:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_alter_pledge_supporter_alter_project_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentCreate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.TextField()),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('author', models.CharField(max_length=200)),
            ],
        ),
    ]
