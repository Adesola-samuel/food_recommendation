import uuid
from django.db import models
from django.contrib.auth.models import User

CHOICES = (
    ('', 'Select'),
    (1, 'Yes'),
    (0, 'No')
)
class Test(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    itching = models.IntegerField(choices = CHOICES)
    skin_rash = models.IntegerField(choices = CHOICES)
    vomiting = models.IntegerField(choices = CHOICES)
    fatigue = models.IntegerField(choices = CHOICES)
    weight_loss = models.IntegerField(choices = CHOICES)
    irregular_sugar_level = models.IntegerField(choices = CHOICES)
    sunken_eyes = models.IntegerField(choices = CHOICES)
    dehydration = models.IntegerField(choices = CHOICES)
    indigestion = models.IntegerField(choices = CHOICES)
    yellowish_skin = models.IntegerField(choices = CHOICES)
    nausea = models.IntegerField(choices = CHOICES)
    loss_of_appetite = models.IntegerField(choices = CHOICES)
    abdominal_pain = models.IntegerField(choices = CHOICES)
    diarrhoea = models.IntegerField(choices = CHOICES)
    yellowing_of_eyes = models.IntegerField(choices = CHOICES)
    blurred_and_distorted_vision = models.IntegerField(choices = CHOICES)
    obesity = models.IntegerField(choices = CHOICES)
    excessive_hunger = models.IntegerField(choices = CHOICES)
    passage_of_gases = models.IntegerField(choices = CHOICES)
    internal_itching = models.IntegerField(choices = CHOICES)
    dischromic_patches = models.IntegerField(choices = CHOICES)
    increased_appetite = models.IntegerField(choices = CHOICES)
    polyuria = models.IntegerField(choices = CHOICES)
    prognosis = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username +' --- '+ self.prognosis

class Message(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message =  models.TextField()
    email =models.EmailField()


    def __str__(self):
        return self.name