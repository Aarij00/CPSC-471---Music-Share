# Generated by Django 4.0.4 on 2022-04-17 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('permissions', models.CharField(default='none', max_length=20)),
                ('admin_id', models.CharField(default='-1', max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('name', models.CharField(default='unknown', max_length=20)),
                ('artist_id', models.CharField(default='-1', max_length=10, primary_key=True, serialize=False)),
                ('p_name', models.CharField(default='-1', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Contains',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_id', models.CharField(default='-1', max_length=10)),
                ('playlist_id', models.CharField(default='-1', max_length=10)),
                ('username', models.CharField(default='-1', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower_id', models.CharField(max_length=10)),
                ('user_id', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='unknown', max_length=100)),
                ('song_id', models.CharField(default='-1', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Manages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id', models.CharField(default='-1', max_length=10)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('mode', models.CharField(default='unknown', max_length=10)),
                ('loudness', models.CharField(default='unknown', max_length=10)),
                ('tempo', models.CharField(default='unknown', max_length=10)),
                ('genre', models.CharField(default='unknown', max_length=20)),
                ('acousticness', models.CharField(default='unknown', max_length=10)),
                ('key', models.CharField(default='-1', max_length=10, primary_key=True, serialize=False)),
                ('danceability', models.CharField(default='unknown', max_length=10)),
                ('duration_ms', models.IntegerField(default=-1)),
                ('energy', models.CharField(default='unknown', max_length=10)),
                ('instrumentalness', models.CharField(default='unknown', max_length=10)),
                ('liveness', models.CharField(default='unknown', max_length=10)),
                ('speechiness', models.CharField(default='unknown', max_length=10)),
                ('time_signature', models.CharField(default='unknown', max_length=10)),
                ('valence', models.CharField(default='unknown', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Moderates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id', models.CharField(default='-1', max_length=10)),
                ('song_id', models.CharField(default='-1', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('playlist_id', models.CharField(default='-1', max_length=10, primary_key=b'I01\n', serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('playlist_name', models.CharField(default='unknown', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='unknown', max_length=100)),
                ('song_id', models.CharField(default='-1', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('name', models.CharField(default='unknown', max_length=20)),
                ('producer_id', models.CharField(default='-1', max_length=10, primary_key=True, serialize=False)),
                ('p_name', models.CharField(default='-1', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProductionLabel',
            fields=[
                ('name', models.CharField(default='-1', max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Releases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_id', models.CharField(default='-1', max_length=10)),
                ('artist_id', models.CharField(default='-1', max_length=10)),
                ('p_name', models.CharField(default='-1', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.CharField(default='-1', max_length=10, primary_key=b'I01\n', serialize=False)),
                ('title', models.CharField(default='unknown', max_length=20)),
                ('duration', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('password', models.CharField(max_length=100)),
                ('biography', models.CharField(max_length=100)),
                ('followers', models.IntegerField()),
                ('following', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserRecommendations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('uRecommendations', models.CharField(max_length=100)),
            ],
        ),
    ]
