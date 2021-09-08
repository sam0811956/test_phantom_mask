from django.db import models

class PharMacies(models.Model):
    name = models.CharField(max_length=100, null=False)
    cashbalance = models.FloatField(null=False)

    def __str__(self):
        return '{0} (cash: {1})'.format(self.name, self.cash_balance)


class Mask(models.Model):
    pharmacies = models.ForeignKey(PharMacies, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    price = models.FloatField(null=False)

    def __str__(self):
        return '{0} (price: {1})'.format(self.name, self.price)

class OpeningHour(models.Model):
    class WeekDay(models.TextChoices):
        MON = "Mon", "Monday"
        TUES = "Tues", "Tuesday"
        WED = "Wed", "Wednesday"
        THURS = "Thurs", "Thursday"
        FRI = "Fri", "Friday"
        SAT = "Sat", "Saturday"
        SUN = "Sun", "Sunday"

    pharmacies = models.ForeignKey(PharMacies, on_delete=models.CASCADE)
    week_day = models.CharField(max_length=5, choices=WeekDay.choices)
    start_hour = models.PositiveSmallIntegerField(null=True)
    start_min = models.PositiveSmallIntegerField(null=True)
    end_hour = models.PositiveSmallIntegerField(null=True)
    end_min = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return '{0} ({1}:{2} - {3}:{4})'.format(
            self.week_day, self.start_hour, self.start_min, self.end_hour, self.end_min
        )
    
