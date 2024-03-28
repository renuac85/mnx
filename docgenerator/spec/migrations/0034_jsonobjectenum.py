# Generated by Django 4.1.5 on 2024-03-28 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spec', '0033_jsonobjectrelationship_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='JSONObjectEnum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField(blank=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='spec.jsonobject')),
            ],
            options={
                'verbose_name': 'JSON object enum value',
                'verbose_name_plural': 'JSON object enum values',
                'db_table': 'json_object_enums',
                'unique_together': {('parent', 'name')},
            },
        ),
    ]
