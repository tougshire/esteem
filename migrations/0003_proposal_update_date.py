# Generated by Django 3.1.3 on 2021-07-18 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esteem', '0002_auto_20210618_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='update_date',
            field=models.DateField(auto_now=True, help_text='When was this proposal created?', verbose_name='updated'),
        ),
    ]
