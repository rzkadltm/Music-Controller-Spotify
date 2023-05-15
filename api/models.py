from django.db import models
import string
import random

def generate_unique_code():
    length = 6
    
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        # code in the left-hand side refers to models, right in the right-hand side for the code above
        if Room.objects.filter(code=code).count() == 0:
            break

    return code

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    # 1 host can only have 1 room
    host = models.CharField(max_length=50, unique=True)
    # null = false meaning gues_can_pause need to has a value
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    