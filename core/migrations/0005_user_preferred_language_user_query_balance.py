# Generated by Django 4.2.10 on 2024-03-10 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_question_options_document_base_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="preferred_language",
            field=models.CharField(
                choices=[("en", "English"), ("pt_BR", "Portugues")],
                default="pt-br",
                max_length=5,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="query_balance",
            field=models.IntegerField(default=100),
        ),
    ]