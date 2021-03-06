# Generated by Django 4.0 on 2022-05-31 05:32

from django.db import migrations, models
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_alter_certifications_date_posted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerFul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corporate', models.CharField(max_length=75)),
                ('role', models.CharField(max_length=50)),
                ('package', models.CharField(max_length=80)),
                ('format', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('registration_open', models.DateField(blank=True, null=True)),
                ('registration_close', models.DateField()),
                ('eligibility', models.TextField()),
                ('referral_link', models.CharField(max_length=100)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('multibranch', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Engineering', 'Engineering'), ('Management', 'Management'), ('Medical and Paramedical', 'Medical and Paramedical'), ('Humanities and Social Sciences', 'Humanities and Social Sciences'), ('Law', 'Law'), ('Sciences', 'Sciences'), ('Pharmacy', 'Pharmacy'), ('Nursing', 'Nursing'), ('Everyone', 'Everyone')], default='Everyone', max_length=116)),
                ('brought_to_you_by', models.CharField(blank=True, choices=[('Student Internship Club', 'Student Internship Club'), ('GCGC', 'GCGC'), ('CGC Visakhapatnam', 'CGC Visakhapatnam'), ('CGC Hyderabad', 'CGC Hyderabad'), ('CGC Bengaluru', 'CGC Bengaluru')], default='Student Internship Club', max_length=70)),
            ],
        ),
        migrations.RemoveField(
            model_name='internship',
            name='branch',
        ),
        migrations.AddField(
            model_name='internship',
            name='brought_to_you_by',
            field=models.CharField(blank=True, choices=[('Student Internship Club', 'Student Internship Club'), ('GCGC', 'GCGC'), ('CGC Visakhapatnam', 'CGC Visakhapatnam'), ('CGC Hyderabad', 'CGC Hyderabad'), ('CGC Bengaluru', 'CGC Bengaluru')], default='Student Internship Club', max_length=70),
        ),
        migrations.AddField(
            model_name='internship',
            name='multibranch',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Engineering', 'Engineering'), ('Management', 'Management'), ('Medical and Paramedical', 'Medical and Paramedical'), ('Humanities and Social Sciences', 'Humanities and Social Sciences'), ('Law', 'Law'), ('Sciences', 'Sciences'), ('Pharmacy', 'Pharmacy'), ('Nursing', 'Nursing'), ('Everyone', 'Everyone')], default='Everyone', max_length=116),
        ),
        migrations.AlterField(
            model_name='scolarships',
            name='branch',
            field=models.CharField(choices=[('Engineering', 'Engineering'), ('Management', 'Management'), ('Medical and Paramedical', 'Medical and Paramedical'), ('Humanities and Social Sciences', 'Humanities and Social Sciences'), ('Law', 'Law'), ('Sciences', 'Sciences'), ('Pharmacy', 'Pharmacy'), ('Nursing', 'Nursing'), ('Everyone', 'Everyone')], default='Everyone', max_length=50),
        ),
    ]
