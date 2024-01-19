# Generated by Django 5.0 on 2024-01-16 06:03

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0005_reporttype_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='paid_payment',
        ),
        migrations.AddField(
            model_name='patient',
            name='paid_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='patient',
            name='remaining_amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='patient',
            name='total_amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='payment_status',
            field=models.CharField(default='Pending', max_length=255),
        ),
        migrations.CreateModel(
            name='paid_installment',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment_id', models.CharField(blank=True, max_length=255, primary_key=True, serialize=False)),
                ('paid_date', models.DateField(default=django.utils.timezone.now)),
                ('paid_payment', models.FloatField()),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.patient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
