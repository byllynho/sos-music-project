# Generated by Django 2.2.6 on 2019-12-07 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191108_2124'),
        ('songs', '0006_songcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='songcomment',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='accounts.Account'),
            preserve_default=False,
        ),
    ]
