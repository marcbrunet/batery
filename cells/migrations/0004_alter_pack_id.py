# Generated by Django 4.1.2 on 2022-10-16 23:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cells', '0003_remove_pack_capacity_alter_pack_id_evaluation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pack',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0413dc3c-4da7-11ed-b0fd-c5c6ef34ccc9'), editable=False, primary_key=True, serialize=False),
        ),
    ]
