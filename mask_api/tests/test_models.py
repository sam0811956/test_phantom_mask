from django.test import TestCase
from mask_api.models import *

class Test_Model(TestCase):
    def test_pharm_model(self):
        pharm = PharMacies.objects.create(
                name = "Better You",
                cashbalance = 777.61
        )
        self.assertEqual(pharm.name, "Better You")
        self.assertEqual(pharm.cashbalance, 777.61)
    def test_mask_model(self):
        pharm = PharMacies.objects.create(
                name = "Better You",
                cashbalance = 777.61,
                )
        mask = Mask.objects.create(
                name = "AniMask (blue) (10 per pack)",
                price = 33.65,
                pharmacies=pharm
                )
        mask = Mask.objects.get(id=1)

        self.assertEqual(mask.pharmacies.name, "Better You")
    def test_openhour_model(self):
        pharm = PharMacies.objects.create(
                name = "Better You",
                cashbalance = 777.61,
                )
        open_hour = OpeningHour.objects.create(
                    pharmacies = pharm,
                    week_day = "Mon",
                    start_hour = 12,
                    start_min = 56,
                    end_hour = 21,
                    end_min = 58
                )
        open_hour = OpeningHour.objects.get(id=1)
        self.assertEqual(open_hour.pharmacies.name, "Better You")

    def test_user_model(self):
        user = User.objects.create(
                name = "Eric Underwood",
                cashbalance = 952.69
                )
        self.assertEqual(user.name, "Eric Underwood")
        self.assertEqual(user.cashbalance, 952.69)

    def test_purchasehistory_model(self):
        user = User.objects.create(
                name = "Eric Underwood",
                cashbalance = 952.69
                )
        purchase = PurchaseHistory.objects.create(
                    user = user,
                    pharmacies_name = "Neighbors",
                    mask_name = "Masquerade (black) (3 per pack)",
                    trans_amount = 9.26,
                    trans_date = "2021-01-02 20:41:02"
                )
        purchase = PurchaseHistory.objects.get(id=1)
        self.assertEqual(purchase.user.name, "Eric Underwood")

