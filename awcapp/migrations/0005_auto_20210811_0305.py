# Generated by Django 3.2.5 on 2021-08-11 03:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('awcapp', '0004_auto_20210811_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='deathinfo',
            name='sector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='awcapp.sector'),
        ),
        migrations.AddField(
            model_name='postpartummother',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='staffinfo',
            name='superviser_name',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Superviser Name'),
        ),
    ]