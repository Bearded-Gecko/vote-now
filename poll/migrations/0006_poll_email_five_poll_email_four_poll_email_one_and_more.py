# Generated by Django 4.2 on 2023-05-10 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0005_rename_current_time_poll_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='email_five',
            field=models.EmailField(default='na@email.com', max_length=254),
        ),
        migrations.AddField(
            model_name='poll',
            name='email_four',
            field=models.EmailField(default='na@email.com', max_length=254),
        ),
        migrations.AddField(
            model_name='poll',
            name='email_one',
            field=models.EmailField(default='na@email.com', max_length=254),
        ),
        migrations.AddField(
            model_name='poll',
            name='email_three',
            field=models.EmailField(default='na@email.com', max_length=254),
        ),
        migrations.AddField(
            model_name='poll',
            name='email_two',
            field=models.EmailField(default='na@email.com', max_length=254),
        ),
    ]