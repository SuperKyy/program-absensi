# Generated by Django 4.2.2 on 2023-10-23 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perizinan', '0001_initial'),
        ('presensi', '0001_initial'),
        ('biodata', '0001_initial'),
        ('absensi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rekap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('absen_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='absensi.absen')),
                ('nama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biodata.biodata')),
                ('perizinan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perizinan.perizinan')),
                ('presensi_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='presensi.presensi')),
            ],
        ),
    ]