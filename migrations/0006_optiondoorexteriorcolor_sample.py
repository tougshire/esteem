# Generated by Django 4.0.2 on 2022-03-26 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esteem', '0005_proposal_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='optiondoorexteriorcolor',
            name='sample',
            field=models.ImageField(blank=True, help_text='What is a sample of the color?', null=True, upload_to='', verbose_name='Sample'),
        ),
    ]
