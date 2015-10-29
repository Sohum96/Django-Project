# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bc', '0003_auto_20151027_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importcandidate',
            name='pref0',
            field=models.CharField(default='', max_length=15, verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='importcandidate',
            name='pref1',
            field=models.CharField(default='', max_length=15, verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='importcandidate',
            name='pref10',
            field=models.CharField(default='', max_length=15, verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='importcandidate',
            name='pref11',
            field=models.CharField(default='', max_length=15, verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='importcandidate',
            name='pref12',
            field=models.CharField(default='', max_length=15, verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='importcandidate',
            name='pref13',
            field=models.CharField(default='', max_length=15, verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='importcandidate',
            name='pref14',
            field=models.CharField(default='', max_length=15, verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='importcandidate',
            name='pref15',
            field=models.CharField(default='', max_length=15, verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='importcandidate',
            name='pref16',
            field=models.CharField(default='', max_length=15, verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='importcandidate',
            name='pref2',
            field=models.CharField(default='', max_length=15, verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='importcandidate',
            name='pref3',
            field=models.CharField(default='', max_length=15, verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='importcandidate',
            name='pref4',
            field=models.CharField(default='', max_length=15, verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='importcandidate',
            name='pref5',
            field=models.CharField(default='', max_length=15, verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='importcandidate',
            name='pref6',
            field=models.CharField(default='', max_length=15, verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='importcandidate',
            name='pref7',
            field=models.CharField(default='', max_length=15, verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='importcandidate',
            name='pref8',
            field=models.CharField(default='', max_length=15, verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='importcandidate',
            name='pref9',
            field=models.CharField(default='', max_length=15, verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
    ]
