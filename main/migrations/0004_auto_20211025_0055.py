# Generated by Django 3.2.5 on 2021-10-24 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211025_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='abdominal_pain',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='blurred_and_distorted_vision',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='dehydration',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='diarrhoea',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='dischromic_patches',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='excessive_hunger',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='fatigue',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='increased_appetite',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='indigestion',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='internal_itching',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='irregular_sugar_level',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='itching',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='loss_of_appetite',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='nausea',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='obesity',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='passage_of_gases',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='polyuria',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='skin_rash',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='sunken_eyes',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='vomiting',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='weight_loss',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='yellowing_of_eyes',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='test',
            name='yellowish_skin',
            field=models.IntegerField(choices=[('', 'Select Gender'), (1, 'Yes'), (0, 'No')]),
        ),
    ]
