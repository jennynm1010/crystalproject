# Generated by Django 2.2 on 2019-06-30 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20190630_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lore', models.TextField(max_length=500)),
            ],
        ),
        migrations.RenameField(
            model_name='crystal',
            old_name='description',
            new_name='mining',
        ),
        migrations.AlterField(
            model_name='charging',
            name='medium',
            field=models.CharField(choices=[('L', 'Lavender'), ('E', 'Earth'), ('W', 'Water'), ('M', 'Moonlight')], default='L', max_length=1),
        ),
        migrations.RemoveField(
            model_name='crystal',
            name='uses',
        ),
        migrations.AddField(
            model_name='crystal',
            name='uses',
            field=models.TextField(default='meditation', max_length=500),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Use',
        ),
        migrations.AddField(
            model_name='crystal',
            name='lore',
            field=models.ManyToManyField(to='main_app.Lore'),
        ),
    ]
