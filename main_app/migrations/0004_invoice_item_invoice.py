# Generated by Django 4.0.6 on 2022-07-14 11:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_item_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название документа')),
                ('created_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Накладная',
                'verbose_name_plural': 'Накладные',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.invoice', verbose_name='Накладная'),
        ),
    ]
