# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-08 01:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, max_length=31)),
                ('first_name', models.CharField(blank=True, max_length=31)),
                ('last_name', models.CharField(blank=True, max_length=31)),
                ('access_token', models.CharField(default='', max_length=512)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128, null=True)),
                ('frequency', models.CharField(default='', max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BookshelfEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=31)),
                ('rating', models.PositiveSmallIntegerField(null=True)),
                ('book', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.Book')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_name', models.CharField(default='', max_length=128)),
                ('start_date', models.CharField(default='', max_length=128)),
                ('end_date', models.CharField(default='', max_length=128)),
                ('contract_type', models.CharField(default='', max_length=128)),
                ('contract_class', models.CharField(default='', max_length=128)),
                ('due_data', models.CharField(default='', max_length=128)),
                ('amount_money', models.CharField(default='', max_length=128)),
                ('auto_extensions', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='DetectionReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('href_to_image', models.CharField(default='', max_length=1024)),
                ('text', models.CharField(default='', max_length=512)),
                ('date', models.CharField(default='', max_length=32)),
                ('type', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimated_price', models.CharField(default='', max_length=32, null=True)),
                ('type', models.CharField(default='', max_length=256, null=True)),
                ('icon', models.CharField(default='', max_length=256, null=True)),
                ('detection_reason', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.DetectionReason')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128, null=True)),
                ('age', models.CharField(default='', max_length=12, null=True)),
                ('gender', models.CharField(default='', max_length=32, null=True)),
                ('relation', models.CharField(default='', max_length=64, null=True)),
                ('detection_reason', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.DetectionReason')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('name_url', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Injury',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='', max_length=32, null=True)),
                ('type', models.CharField(default='', max_length=128, null=True)),
                ('detection_reason', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.DetectionReason')),
            ],
        ),
        migrations.CreateModel(
            name='LifestyleEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128, null=True)),
                ('frequency', models.CharField(default='', max_length=64, null=True)),
                ('detection_reason', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.DetectionReason')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=256, null=True)),
                ('example_image', models.CharField(default='', max_length=1024, null=True)),
                ('detection_reason', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.DetectionReason')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Group')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb_access_token', models.CharField(default='', max_length=512, null=True)),
                ('lfd_id', models.CharField(blank=True, max_length=12, null=True)),
                ('parent_lfd_id', models.CharField(blank=True, max_length=12, null=True)),
                ('pnr_nr', models.CharField(blank=True, max_length=12, null=True)),
                ('title', models.CharField(blank=True, max_length=12, null=True)),
                ('given_name', models.CharField(blank=True, max_length=128, null=True)),
                ('surname', models.CharField(blank=True, max_length=128, null=True)),
                ('gender', models.CharField(blank=True, max_length=32, null=True)),
                ('email_address', models.CharField(blank=True, max_length=256, null=True)),
                ('browser_user_agent', models.CharField(blank=True, max_length=512, null=True)),
                ('telephone_number', models.CharField(blank=True, max_length=64, null=True)),
                ('telephone_country_code', models.CharField(blank=True, max_length=12, null=True)),
                ('birthday', models.CharField(blank=True, max_length=24, null=True)),
                ('age', models.CharField(blank=True, max_length=3, null=True)),
                ('tropical_zodiac', models.CharField(blank=True, max_length=64, null=True)),
                ('cc_type', models.CharField(blank=True, max_length=64, null=True)),
                ('cc_number', models.CharField(blank=True, max_length=64, null=True)),
                ('cvv2', models.CharField(blank=True, max_length=12, null=True)),
                ('cc_expires', models.CharField(blank=True, max_length=64, null=True)),
                ('occupation', models.CharField(blank=True, max_length=256, null=True)),
                ('company', models.CharField(blank=True, max_length=256, null=True)),
                ('vehicle', models.CharField(blank=True, max_length=256, null=True)),
                ('domain', models.CharField(blank=True, max_length=256, null=True)),
                ('blood_type', models.CharField(blank=True, max_length=12, null=True)),
                ('pounds', models.CharField(blank=True, max_length=12, null=True)),
                ('kilograms', models.CharField(blank=True, max_length=12, null=True)),
                ('feet_inches', models.CharField(blank=True, max_length=12, null=True)),
                ('centimeters', models.CharField(blank=True, max_length=3, null=True)),
                ('profile_picture', models.CharField(blank=True, max_length=512, null=True)),
                ('maried', models.CharField(blank=True, max_length=64, null=True)),
                ('kids', models.CharField(blank=True, max_length=12, null=True)),
                ('income', models.CharField(blank=True, max_length=64, null=True)),
                ('expenses', models.CharField(blank=True, max_length=64, null=True)),
                ('fitness', models.CharField(blank=True, max_length=128, null=True)),
                ('home_town', models.CharField(blank=True, max_length=512, null=True)),
                ('country', models.CharField(blank=True, max_length=256, null=True)),
                ('education', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('stars', models.FloatField()),
                ('date', models.CharField(default='', max_length=32)),
                ('contract', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Contract')),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Person')),
            ],
        ),
        migrations.CreateModel(
            name='SalaryMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.CharField(default='', max_length=256)),
                ('salary', models.CharField(default='', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='', max_length=256)),
                ('content', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success', models.CharField(default='0', max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Person'),
        ),
        migrations.AddField(
            model_name='lifestyleentity',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Person'),
        ),
        migrations.AddField(
            model_name='injury',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Person'),
        ),
        migrations.AddField(
            model_name='familymember',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Person'),
        ),
        migrations.AddField(
            model_name='device',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Person'),
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together=set([('title', 'author')]),
        ),
        migrations.AddField(
            model_name='activity',
            name='detection_reason',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.DetectionReason'),
        ),
        migrations.AddField(
            model_name='activity',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Person'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Person'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together=set([('user', 'group')]),
        ),
        migrations.AlterUniqueTogether(
            name='bookshelfentry',
            unique_together=set([('user', 'book')]),
        ),
    ]
