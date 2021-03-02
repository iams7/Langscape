from django.db import models

# Create your models here.
class Headword(models.Model):
    word = models.CharField(max_length=45)

    def __str__(self):
        return self.word

pos_choices = (
    ("noun", "Noun"),
    ("verb", "Verb"),
    ("adverb", "Adverb"),
    ("adjective", "Adjective")
)

class POS(models.Model):

    word = models.ForeignKey(Headword, on_delete=models.CASCADE, related_name='meanings')
    part_of_speech = models.CharField(choices=pos_choices, max_length=10, null=False)

    def __str__(self):
        return f"{self.word} as {self.part_of_speech}"

    class Meta:
        unique_together = ('word', 'part_of_speech')
        index_together = ('word','part_of_speech')

class Meaning(models.Model):
    pos = models.ForeignKey(POS, on_delete=models.CASCADE, related_name='dictionary_meanings')
    meaning = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.id} - {self.pos} - {self.meaning}"