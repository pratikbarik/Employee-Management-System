# Generated by Django 5.0.6 on 2024-05-21 06:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('LeaveId', models.AutoField(primary_key=True, serialize=False)),
                ('LeaveType', models.CharField(max_length=5)),
                ('LeaveDays', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserMaster',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Phone', models.BigIntegerField()),
                ('Password', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=10)),
                ('Role', models.CharField(max_length=20)),
                ('Status', models.CharField(default='active', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ApplyLeave',
            fields=[
                ('ApplyLeaveId', models.AutoField(primary_key=True, serialize=False)),
                ('ToDate', models.DateField()),
                ('FromDate', models.DateField()),
                ('Reason', models.CharField(max_length=200)),
                ('LeaveStatus', models.CharField(default='NotApproved', max_length=20)),
                ('LeaveId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.leave')),
                ('UserId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.usermaster')),
            ],
        ),
    ]
