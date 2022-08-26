# Generated by Django 4.1 on 2022-08-25 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ppg_predictor", "0004_auto_20220819_1440"),
    ]

    operations = [
        migrations.CreateModel(
            name="Team",
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
                ("teamname", models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name="player",
            name="currentteam",
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
    ]
