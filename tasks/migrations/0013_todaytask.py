# Generated by Django 3.1.3 on 2020-11-28 19:39

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_nextweektask'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodayTask',
            fields=[
            ],
            options={
                'ordering': ['status', '-priority'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('tasks.task',),
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
