# Generated by Django 4.1.2 on 2023-10-09 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, unique=True)),
                ('balance', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='TraderData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('profit_loss', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('trader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauth.trader')),
            ],
        ),
    ]
