# Generated by Django 3.2.4 on 2021-09-26 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]