# Generated by Django 4.2.5 on 2023-09-23 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0005_alter_article_article_image_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article", options={"ordering": ["-created_date"]},
        ),
        migrations.AlterModelOptions(
            name="comment", options={"ordering": ["-comment_date"]},
        ),
    ]