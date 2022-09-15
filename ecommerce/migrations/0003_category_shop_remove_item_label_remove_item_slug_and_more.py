# Generated by Django 4.1.1 on 2022-09-15 08:46

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="created_at")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="updated_at")),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Shop",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="created_at")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="updated_at")),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="")),
                ("gather_link", models.URLField(blank=True, max_length=500, null=True)),
                ("gather_password", models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RemoveField(
            model_name="item",
            name="label",
        ),
        migrations.RemoveField(
            model_name="item",
            name="slug",
        ),
        migrations.AlterField(
            model_name="item",
            name="category",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="ecommerce.category"),
        ),
    ]
