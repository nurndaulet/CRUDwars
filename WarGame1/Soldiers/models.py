from django.db import models


class Faction(models.Model):
    name = models.CharField(max_length=100)
    flag = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class ArmyType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Army(models.Model):
    commander_name = models.CharField(max_length=100)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)
    left_army = models.ForeignKey(ArmyType, related_name='left_army', on_delete=models.CASCADE)
    center_army = models.ForeignKey(ArmyType, related_name='center_army', on_delete=models.CASCADE)
    right_army = models.ForeignKey(ArmyType, related_name='right_army', on_delete=models.CASCADE)
    victories = models.IntegerField(default=0)
    defeats = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.commander_name} - {self.faction}'

