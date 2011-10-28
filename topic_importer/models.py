from django.db import models


class movie_topic(models.Model):
    movie_name = models.CharField(max_length=255)
    imdb_id = models.CharField(max_length=50)

    def __unicode__(self):
        return self.movie_name
    