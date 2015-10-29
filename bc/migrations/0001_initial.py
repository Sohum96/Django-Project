# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(default='None', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')], verbose_name='Name', max_length=150)),
                ('is_public', models.BooleanField(default=False, verbose_name='Public')),
                ('date_created', models.DateTimeField(verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(verbose_name='Date Updated')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='branches', verbose_name='owner')),
            ],
            options={
                'ordering': ['date_created'],
                'verbose_name_plural': 'branches',
                'verbose_name': 'branch',
            },
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('roll_no', models.CharField(default='15xxxxxxx', verbose_name='Roll No', max_length=20)),
                ('u_name', models.CharField(default='Name', verbose_name='Your Name', max_length=30)),
                ('p_branch', models.CharField(default='None', choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')], verbose_name='Present Branch', max_length=150)),
                ('cpi', models.DecimalField(default=10.0, max_digits=5, verbose_name='CPI', decimal_places=2)),
                ('cat', models.CharField(default='GE', choices=[('GE', 'GE'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST')], verbose_name='Your Category', max_length=30)),
                ('is_public', models.BooleanField(default=False, verbose_name='Public')),
                ('date_created', models.DateTimeField(verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(verbose_name='Date Updated')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='candidates', verbose_name='owner')),
            ],
            options={
                'verbose_name_plural': 'candidates',
                'verbose_name': 'candidate',
            },
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('rank', models.CharField(max_length=150)),
                ('institute', models.CharField(choices=[('Indian Institute of Technology Bhubaneswar', 'Indian Institute of Technology Bhubaneswar'), ('Indian Institute of Technology Bombay', 'Indian Institute of Technology Bombay'), ('Indian Institute of Technology Delhi', 'Indian Institute of Technology Delhi'), ('Indian Institute of Technology Gandhinagar', 'Indian Institute of Technology Gandhinagar'), ('Indian Institute of Technology Guwahati', 'Indian Institute of Technology Guwahati'), ('Indian Institute of Technology Hyderabad', 'Indian Institute of Technology Hyderabad'), ('Indian Institute of Technology Indore', 'Indian Institute of Technology Indore'), ('Indian Institute of Technology Kanpur', 'Indian Institute of Technology Kanpur'), ('Indian Institute of Technology Kharagpur', 'Indian Institute of Technology Kharagpur'), ('Indian Institute of Technology Madras', 'Indian Institute of Technology Madras'), ('Indian Institute of Technology Mandi', 'Indian Institute of Technology Mandi'), ('Indian Institute of Technology Patna', 'Indian Institute of Technology Patna'), ('Indian Institute of Technology Rajasthan', 'Indian Institute of Technology Rajasthan'), ('Indian Institute of Technology Roorkee', 'Indian Institute of Technology Roorkee'), ('Indian Institute of Technology Ropar', 'Indian Institute of Technology Ropar'), ('Indian School of Mines, Dhanbad', 'Indian School of Mines, Dhanbad'), ('Institute of Technology, Banaras Hindu University,Varanasi', 'Institute of Technology, Banaras Hindu University,Varanasi')], verbose_name='Institute', max_length=150)),
                ('category', models.CharField(choices=[('GE', 'GE'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST')], verbose_name='Category', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('query', models.CharField(choices=[('AE B.Tech', 'AE B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CH', 'CH'), ('CL B.Tech', 'CL B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP B.Tech', 'EP B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME B.Tech', 'ME B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM B.Tech', 'MM B.Tech'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2')], verbose_name='Branch', max_length=150)),
                ('category', models.CharField(choices=[('GE', 'GE'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST')], verbose_name='Category', max_length=10)),
            ],
        ),
    ]
