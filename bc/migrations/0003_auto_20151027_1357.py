# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bc', '0002_delete_prediction'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportCandidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('roll_no', models.CharField(max_length=20, default='15xxxxxxx', verbose_name='Roll No')),
                ('u_name', models.CharField(max_length=30, default='Name', verbose_name='Your Name')),
                ('p_branch', models.CharField(max_length=150, default='AE B.Tech', verbose_name='Present Branch', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')])),
                ('cpi', models.DecimalField(default=10.0, decimal_places=2, verbose_name='CPI', max_digits=5)),
                ('cat', models.CharField(max_length=30, default='GE', verbose_name='Your Category', choices=[('GE', 'GE'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST')])),
                ('is_public', models.BooleanField(default=False, verbose_name='Public')),
                ('pref0', models.CharField(max_length=15, default='None', verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')])),
                ('pref1', models.CharField(max_length=15, default='None', verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')])),
                ('pref2', models.CharField(max_length=15, default='None', verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')])),
                ('pref3', models.CharField(max_length=15, default='None', verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')])),
                ('pref4', models.CharField(max_length=15, default='None', verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')])),
                ('pref5', models.CharField(max_length=15, default='None', verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')])),
                ('pref6', models.CharField(max_length=15, default='None', verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')])),
                ('pref7', models.CharField(max_length=15, default='None', verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')])),
                ('pref8', models.CharField(max_length=15, default='None', verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')])),
                ('pref9', models.CharField(max_length=15, default='None', verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')])),
                ('pref10', models.CharField(max_length=15, default='None', verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')])),
                ('pref11', models.CharField(max_length=15, default='None', verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')])),
                ('pref12', models.CharField(max_length=15, default='None', verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')])),
                ('pref13', models.CharField(max_length=15, default='None', verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')])),
                ('pref14', models.CharField(max_length=15, default='None', verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')])),
                ('pref15', models.CharField(max_length=15, default='None', verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')])),
                ('pref16', models.CharField(max_length=15, default='None', verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')])),
            ],
            options={
                'verbose_name_plural': 'Icandidates',
                'verbose_name': 'Icandidate',
            },
        ),
        migrations.AlterField(
            model_name='branches',
            name='name',
            field=models.CharField(max_length=30, default='None', verbose_name='Name', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='p_branch',
            field=models.CharField(max_length=30, default='AE B.Tech', verbose_name='Present Branch', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
        migrations.AlterField(
            model_name='query',
            name='query',
            field=models.CharField(max_length=30, verbose_name='Branch', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')]),
        ),
    ]
