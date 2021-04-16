# Generated by Django 3.2 on 2021-04-15 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=5)),
                ('mobile', models.CharField(max_length=13)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_reg.course')),
            ],
        ),
    ]
