from django.contrib.auth.models import User
from django.db import models


class Mood(models.Model):
    VERY_HAPPY = 0
    HAPPY = 1
    MEH = 2
    SAD = 3
    VERY_SAD = 4
    MOOD_CHOICES = (
        (VERY_HAPPY, 'Very Happy'),
        (HAPPY, 'Happy'),
        (MEH, 'Meh'),
        (SAD, 'Sad'),
        (VERY_SAD, 'Very Sad'),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='moods')
    date = models.DateField()
    mood_level = models.IntegerField(choices=MOOD_CHOICES, default=0)
    comment = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.user} - {self.date} - {self.get_mood_level_display()
                                              } - {self.comment}'
