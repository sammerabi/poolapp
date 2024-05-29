from django.db import models

# Create your models here.
class Game(models.Model):
   
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    players = models.ManyToManyField(Player, through='GamePlayer')
    game_date = models.DateTimeField(auto_now_add=True)
    innings = models.SmallIntegerField()

class Player(models.Model):
   
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

class GamePlayer(models.Model):
    
    player= models.ForeignKey(Player, on_delete=models.CASCASE)
    game= models.ForeignKey(Game, on_delete=models.CASCASE)
    score = models.SmallIntegerField(default=0)

    class Meta:
        unique_together = (('player', 'game'),)

    def __str__(self):
        return f"{self.player.first_name} {self.player.last_name} in {self.game.name} with score of {self.score)"
