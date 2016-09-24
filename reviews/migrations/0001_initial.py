# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 23:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('actor_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, verbose_name="Actor's first name")),
                ('last_name', models.CharField(max_length=50, verbose_name="Actor's last name")),
                ('date_of_birth', models.DateField(verbose_name="Actor's DOB")),
            ],
            options={
                'db_table': 'Actor',
            },
        ),
        migrations.CreateModel(
            name='ActorPlays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Actor')),
            ],
            options={
                'db_table': 'ActorPlays',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('director_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Director',
            },
        ),
        migrations.CreateModel(
            name='Directs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Director')),
            ],
            options={
                'db_table': 'Directs',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70, unique=True, verbose_name="Movie's name")),
                ('trailer_url', models.URLField(default='https://www.youtube.com/', verbose_name="Movie's Trailer")),
                ('poster_url', models.URLField(default='', verbose_name="Movie's Poster")),
                ('date_released', models.DateField(verbose_name="Movie's Release Date")),
            ],
            options={
                'db_table': 'Movie',
            },
        ),
        migrations.CreateModel(
            name='MovieTopics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
                ('subtitles', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Movie')),
            ],
            options={
                'db_table': 'MovieTopics',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('user_name', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=200)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Actor')),
            ],
            options={
                'db_table': 'Role',
            },
        ),
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Movie')),
            ],
            options={
                'db_table': 'Sponsors',
            },
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('studio_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('movies', models.ManyToManyField(through='reviews.Sponsors', to='reviews.Movie')),
            ],
            options={
                'db_table': 'Studio',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Topic',
            },
        ),
        migrations.AddField(
            model_name='sponsors',
            name='studio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Studio'),
        ),
        migrations.AddField(
            model_name='movietopics',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Topic'),
        ),
        migrations.AddField(
            model_name='movie',
            name='topics',
            field=models.ManyToManyField(through='reviews.MovieTopics', to='reviews.Topic'),
        ),
        migrations.AddField(
            model_name='directs',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Movie'),
        ),
        migrations.AddField(
            model_name='director',
            name='movies',
            field=models.ManyToManyField(through='reviews.Directs', to='reviews.Movie'),
        ),
        migrations.AddField(
            model_name='actorplays',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Movie'),
        ),
        migrations.AddField(
            model_name='actor',
            name='movies',
            field=models.ManyToManyField(through='reviews.ActorPlays', to='reviews.Movie'),
        ),
        migrations.AlterUniqueTogether(
            name='sponsors',
            unique_together=set([('studio', 'movie')]),
        ),
        migrations.AlterUniqueTogether(
            name='movietopics',
            unique_together=set([('movie', 'topic')]),
        ),
        migrations.AlterUniqueTogether(
            name='directs',
            unique_together=set([('director', 'movie')]),
        ),
        migrations.AlterUniqueTogether(
            name='actorplays',
            unique_together=set([('movie', 'actor')]),
        ),
    ]