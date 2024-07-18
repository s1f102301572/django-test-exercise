from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('todo', '0001_initial'),
    ]
    operations = [
        migrations.AddField(
            model_name='task',
            name='note',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]