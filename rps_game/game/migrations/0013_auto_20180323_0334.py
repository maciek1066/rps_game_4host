# Generated by Django 2.0.3 on 2018-03-23 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_auto_20180323_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='creator_move',
            field=models.IntegerField(blank=True, choices=[(3, 'scissors'), (1, 'rock'), (2, 'paper')], null=True),
        ),
        migrations.AlterField(
            model_name='round',
            name='opponent_move',
            field=models.IntegerField(blank=True, choices=[(3, 'scissors'), (1, 'rock'), (2, 'paper')], null=True),
        ),
    ]
