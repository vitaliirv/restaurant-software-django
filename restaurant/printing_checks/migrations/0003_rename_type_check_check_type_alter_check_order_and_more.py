# Generated by Django 4.1.4 on 2022-12-22 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printing_checks', '0002_alter_check_status_alter_check_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='check',
            old_name='type',
            new_name='check_type',
        ),
        migrations.AlterField(
            model_name='check',
            name='order',
            field=models.JSONField(blank=True, verbose_name='Інформація про замовлення'),
        ),
        migrations.AlterField(
            model_name='check',
            name='pdf_file',
            field=models.FileField(blank=True, upload_to='pdf', verbose_name='Посилання на PDF'),
        ),
    ]
