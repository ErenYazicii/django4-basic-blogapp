# Generated by Django 4.2.5 on 2023-09-23 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0004_alter_article_article_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="article_image",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="documents/",
                verbose_name="Makaleye Fotoğraf Ekleyin",
            ),
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "comment_author",
                    models.CharField(max_length=50, verbose_name="isim"),
                ),
                (
                    "comment_content",
                    models.CharField(max_length=200, verbose_name="yorum"),
                ),
                ("comment_date", models.DateTimeField(auto_now_add=True)),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="article.article",
                        verbose_name="Makale",
                    ),
                ),
            ],
        ),
    ]
