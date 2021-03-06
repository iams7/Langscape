# Generated by Django 3.1.7 on 2021-03-01 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pos',
            name='part_name',
            field=models.CharField(choices=[('noun', 'Noun'), ('verb', 'Verb'), ('adverb', 'Adverb'), ('adjective', 'Adjective')], max_length=10),
        ),
        migrations.CreateModel(
            name='Meaning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meaning', models.TextField(max_length=500)),
                ('pos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictApp.pos')),
            ],
        ),
    ]
