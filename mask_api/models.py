from django.db import models

class PharMacies(models.Model):
    name = models.CharField(max_length=100, null=False)
    cashbalance = models.FloatField(null=False)
#    objects = PharMaciesManager()
#objects = models.Manager()

    def __str__(self):
        return '{0} (cash: {1})'.format(self.name, self.cashbalance)


class Mask(models.Model):
    pharmacies = models.ForeignKey(PharMacies, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    price = models.FloatField(null=False)
#objects = MaskManager()
#objects = models.Manager()

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
#objects = models.Manager()
#objects = OpeningHourManager()

    def __str__(self):
        return '{0} ({1}:{2} - {3}:{4})'.format(
            self.week_day, self.start_hour, self.start_min, self.end_hour, self.end_min
        )
    
class User(models.Model):
    name = models.CharField(max_length=100, null=False)
    cashbalance = models.FloatField(null=False)

    def __str__(self):
        return '{0} (cashbalance: {1})'.format(self.name, self.cashbalance)

class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchasehistory', null=True, blank=True)
    pharmacies_name = models.CharField(max_length=100, null=False)
    mask_name = models.CharField(max_length=100, null=False)
    trans_amount = models.FloatField(null=False)
    trans_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'pharmacies_name: {0}, mask_name: {1}, (amount: {2}, date: {3})'.format(
            self.pharmacies_name, self.mask_name, self.trans_amount,
            self.trans_date)
