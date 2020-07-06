# Generated by Django 3.0.7 on 2020-07-06 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeScore', models.IntegerField()),
                ('serviceScore', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('images', models.TextField(blank=True)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('modifiedAt', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Service')),
            ],
        ),
    ]