# Generated by Django 4.1.7 on 2023-04-02 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0005_alter_vote_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='object_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vote',
            name='user_id',
            field=models.CharField(max_length=50),
        ),
    ]
