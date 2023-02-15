# Generated by Django 2.2.24 on 2023-02-14 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0008_auto_20220907_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='releasefile',
            name='sigstore_bundle_file',
            field=models.URLField(blank=True, help_text='Sigstore Bundle URL', verbose_name='Sigstore Bundle URL'),
        ),
    ]