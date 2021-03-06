# Generated by Django 2.2.5 on 2020-06-23 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vps', '0017_auto_20200623_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='connect_pid',
            field=models.IntegerField(choices=[(0, '否'), (1, '是')], default=1, max_length=1, verbose_name='是否需要连接PID'),
        ),
        migrations.AlterField(
            model_name='company',
            name='need_monitor',
            field=models.IntegerField(choices=[(0, '否'), (1, '是')], default=1, max_length=1, verbose_name='是否需要监控'),
        ),
    ]
