# Generated by Django 4.2.5 on 2023-10-10 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('calculo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='user',
        ),
        migrations.AddField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(related_name='usuarios', to='auth.group'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(related_name='usuarios', to='auth.permission'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
