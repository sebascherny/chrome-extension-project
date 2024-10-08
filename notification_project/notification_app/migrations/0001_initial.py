# Generated by Django 4.0.1 on 2024-09-12 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('displayed', 'Displayed'), ('acknowledged', 'Acknowledged'), ('dismissed', 'Dismissed')], max_length=20)),
                ('url', models.URLField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
