# Generated by Django 3.2.4 on 2021-10-13 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0002_alter_course_course_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='thumb_nail',
            field=models.FileField(default=None, upload_to='static/'),
            preserve_default=False,
        ),
    ]