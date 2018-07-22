import string

from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.postgres.fields.array import ArrayField
from django.db import models


class PostManager(models.Manager):
    def create(self, author, title, html, content_warnings=None):
        """
        Save blog posts to PostgreSQL.
        Args:
            author (str): author of post
            title (str): title of post as it will appear in post
            content_warnings (str, optional): Defaults to None. list of warning triggers
            published_date_utc (datetime.date, optional): Defaults to None. date of published date in UTC
        Returns:
            Post
        """
        post = Post()
        post.author = author
        post.title = title
        post.html = html
        post.created_at_utc = datetime.utcnow()
        post.content_warnings = self.string_to_array(content_warnings) if content_warnings else None
        post.url = self.create_url(author=post.author, title=post.title, created_at_utc=post.created_at_utc)
        post.save()
        return post

    def create_url(self, title, author, created_at_utc):
        return '/'.join(map(self.format_comp_string, ['post', str(created_at_utc.year), author, title]))

    @staticmethod
    def format_comp_string(human_string):
        """
        Remove all punctuation, makes it lowercase, and replaces spaces with hyphens.
        Args:
            human_string (str): human-readable string
        Returns:
            str: computer-readable string
        """
        human_string = human_string.replace(' ', '-').lower()
        return "".join(x for x in human_string if x == '-' or x not in string.punctuation)

    @staticmethod
    def string_to_array(array_string):
        """
        Convert comma-separated string to array.
        Args:
            array_string (str): comma-separated string
        Returns:
            list: list of strings
        """
        if array_string:
            return [x.strip(')(][ ').lower() for x in array_string.split(',')]
        return None


class Post(models.Model):
    author = models.TextField()
    title = models.TextField()
    created_at_utc = models.DateTimeField(auto_now_add=True)
    content_warnings = ArrayField(models.TextField(), null=True, blank=True)
    url = models.TextField(primary_key=True)
    html = models.TextField()
    num_views = models.IntegerField(default=0)

    objects = PostManager()

    class Meta:
        db_table = "post"


class DiscussionTopic(models.Model):
    summary = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # renames to author_id in table
    created_at_utc = models.DateTimeField(auto_now_add=True)
    elaboration = models.TextField()

    objects = models.Manager()

    class Meta:
        db_table = "discussion_topic"
