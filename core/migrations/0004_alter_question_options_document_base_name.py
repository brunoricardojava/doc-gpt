# Generated by Django 4.2.10 on 2024-03-05 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_question_cost"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="question",
            options={"ordering": ["-id"]},
        ),
        migrations.AddField(
            model_name="document",
            name="base_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]