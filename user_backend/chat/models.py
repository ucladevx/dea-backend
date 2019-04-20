from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Room(models.Model):
    user1 = models.ForeignKey('users.User', on_delete=models.CASCADE, default="6", related_name="user_1")
    user2 = models.ForeignKey('users.User', on_delete=models.CASCADE, default="8", related_name="user_2")

    name = models.TextField()
    label = models.SlugField(unique=True)
    users = models.TextField(null=True)

    key = models.TextField(null=True)

    def __unicode__(self):
        return self.label


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE,)
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __unicode__(self):
        return '[{timestamp}] {handle}: {message}'.format(**self.as_dict())

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%b %-d %-I:%M %p')

    def as_dict(self):
        return {'handle': self.handle, 'message': self.message, 'timestamp': self.formatted_timestamp}
