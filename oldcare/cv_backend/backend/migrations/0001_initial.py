# Generated by Django 2.2.6 on 2022-07-10 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='employee_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ORG_ID', models.IntegerField(blank=True, null=True)),
                ('CLIENT_ID', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(max_length=50)),
                ('gender', models.CharField(blank=True, max_length=5)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('id_card', models.CharField(blank=True, max_length=50)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('checkin_date', models.DateField(blank=True, null=True)),
                ('checkout_data', models.DateField(blank=True, null=True)),
                ('imgset_dir', models.CharField(blank=True, max_length=200)),
                ('profile_photo', models.CharField(blank=True, max_length=200)),
                ('DESCRIPTION', models.CharField(blank=True, max_length=200)),
                ('ISACTIVE', models.CharField(blank=True, max_length=10)),
                ('CREATED', models.DateTimeField(blank=True, null=True)),
                ('CREATEBY', models.CharField(blank=True, max_length=50, null=True)),
                ('UPDATED', models.DateTimeField(blank=True, null=True)),
                ('UPDATEBY', models.CharField(blank=True, max_length=50, null=True)),
                ('REMOVE', models.CharField(blank=True, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='oldperson_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ORG_ID', models.IntegerField(blank=True, null=True)),
                ('CLIENT_ID', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(max_length=50)),
                ('gender', models.CharField(blank=True, max_length=5)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('id_card', models.CharField(blank=True, max_length=50)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('checkin_date', models.DateField(blank=True, null=True)),
                ('checkout_data', models.DateField(blank=True, null=True)),
                ('imgset_dir', models.CharField(blank=True, max_length=200)),
                ('profile_photo', models.CharField(blank=True, max_length=200)),
                ('room_number', models.CharField(blank=True, max_length=50)),
                ('firstguardian_name', models.CharField(blank=True, max_length=50)),
                ('firstguardian_relationship', models.CharField(blank=True, max_length=50)),
                ('firstguardian_phone', models.CharField(blank=True, max_length=50)),
                ('firstguardian_wechat', models.CharField(blank=True, max_length=50)),
                ('sceondguardian_name', models.CharField(blank=True, max_length=50)),
                ('secondguardian_relationship', models.CharField(blank=True, max_length=50)),
                ('secondguardian_phone', models.CharField(blank=True, max_length=50)),
                ('secondguardian_wechat', models.CharField(blank=True, max_length=50)),
                ('health_state', models.CharField(blank=True, max_length=50)),
                ('DESCRIPTION', models.CharField(blank=True, max_length=50)),
                ('ISACTIVE', models.CharField(blank=True, max_length=10)),
                ('CREATED', models.DateTimeField(blank=True, null=True)),
                ('CREATEBY', models.CharField(blank=True, max_length=50, null=True)),
                ('UPDATED', models.DateTimeField(blank=True, null=True)),
                ('UPDATEBY', models.CharField(blank=True, max_length=50, null=True)),
                ('REMOVE', models.CharField(blank=True, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='volunteer_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ORG_ID', models.IntegerField(blank=True, null=True)),
                ('CLIENT_ID', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(max_length=50)),
                ('gender', models.CharField(blank=True, max_length=5)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('id_card', models.CharField(blank=True, max_length=50)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('checkin_date', models.DateField(blank=True, null=True)),
                ('checkout_date', models.DateField(blank=True, null=True)),
                ('imgset_dir', models.CharField(blank=True, max_length=200)),
                ('profile_photo', models.CharField(blank=True, max_length=200)),
                ('DESCRIPTION', models.CharField(blank=True, max_length=200)),
                ('ISACTIVE', models.CharField(blank=True, max_length=10)),
                ('CREATED', models.DateTimeField(blank=True, null=True)),
                ('CREATEBY', models.CharField(blank=True, max_length=50, null=True)),
                ('UPDATED', models.DateTimeField(blank=True, null=True)),
                ('UPDATEBY', models.CharField(blank=True, max_length=50, null=True)),
                ('REMOVE', models.CharField(blank=True, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='sys_user',
            fields=[
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='backend.Account')),
                ('ORG_ID', models.IntegerField(blank=True, null=True)),
                ('CLIENT_ID', models.IntegerField(blank=True, null=True)),
                ('REAL_NAME', models.CharField(blank=True, max_length=50)),
                ('SEX', models.CharField(blank=True, max_length=20)),
                ('EMAIL', models.CharField(blank=True, max_length=50)),
                ('PHONE', models.CharField(blank=True, max_length=50)),
                ('MOBILE', models.CharField(blank=True, max_length=50)),
                ('DESCRIPTION', models.CharField(blank=True, max_length=200)),
                ('ISACTIVE', models.CharField(blank=True, max_length=10)),
                ('CREATED', models.DateTimeField(blank=True, null=True)),
                ('CREATEBY', models.CharField(blank=True, max_length=50, null=True)),
                ('UPDATED', models.DateTimeField(blank=True, null=True)),
                ('UPDATEBY', models.CharField(blank=True, max_length=50, null=True)),
                ('REMOVE', models.CharField(blank=True, max_length=1)),
                ('DATAFILTER', models.CharField(blank=True, max_length=200)),
                ('theme', models.CharField(blank=True, max_length=45)),
                ('defaultpage', models.CharField(blank=True, max_length=45)),
                ('logoimage', models.CharField(blank=True, max_length=45)),
                ('qqopenid', models.CharField(blank=True, max_length=100)),
                ('appversion', models.CharField(blank=True, max_length=10)),
                ('jsonauth', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='event_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event_type', models.IntegerField(blank=True, null=True)),
                ('event_date', models.DateField(auto_now=True, null=True)),
                ('event_location', models.CharField(blank=True, max_length=200)),
                ('event_desc', models.CharField(default='', max_length=200)),
                ('img_path', models.CharField(blank=True, max_length=200)),
                ('oldperson_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person', to='backend.oldperson_info')),
            ],
        ),
    ]
