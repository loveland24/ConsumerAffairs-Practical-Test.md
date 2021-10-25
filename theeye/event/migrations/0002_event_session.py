# Generated by Django 2.2.24 on 2021-10-25 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='session.Session'),
        ),
    ]