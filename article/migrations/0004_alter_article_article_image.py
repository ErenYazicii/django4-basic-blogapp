# Generated by Django 4.2.5 on 2023-09-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0003_alter_article_article_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="article_image",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="",
                verbose_name="Makaleye Fotoğraf Ekleyin",
            ),
        ),
    ]