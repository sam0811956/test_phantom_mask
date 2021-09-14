from django.test import TestCase, Client
from django.urls import reverse
import json

class Test_View(TestCase):
    def setUp(self):
        self.client = Client()

    def test_find_pharm_open_weekday_hour(self):
        test_url = reverse('find_pharm_open_weekday_hour')
        test_data = {'weekday': 'Mon', 'hour': 10, 'min': 10}
        result_data = ['Apotheco', 'Drug Blend']
        response = self.client.get(test_url, test_data)
        response_json = json.loads(response.content)['open_pharmacies']

        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(response_json, result_data)

    def test_find_pharm_sold_mask_sort(self):
        test_url = reverse('find_pharm_sold_mask_sort')
        test_data_name = {"pharm": "Cash Saver Pharmacy", "sort": "name"}
        test_data_price = {"pharm": "Cash Saver Pharmacy", "sort": "price"}
        result_price = ['Free to Roam (black) (3 per pack) (price: 13.83)',
                        'MaskT (black) (10 per pack) (price: 14.9)',
                        'Masquerade (blue) (6 per pack) (price: 16.75)',
                        'AniMask (green) (10 per pack) (price: 49.21)'
                        ]
        result_name = ['AniMask (green) (10 per pack) (price: 49.21)',
                       'Free to Roam (black) (3 per pack) (price: 13.83)',
                       'MaskT (black) (10 per pack) (price: 14.9)',
                       'Masquerade (blue) (6 per pack) (price: 16.75)'
                       ]

        response_name = self.client.get(test_url, test_data_name)
        response_name_json = json.loads(response_name.content)['mask_sort']
        response_price = self.client.get(test_url, test_data_price)
        response_price_json = json.loads(response_price.content)['mask_sort']

        self.assertEqual(response_name.status_code, 200)
        self.assertEqual(response_name_json, result_name)
        self.assertEqual(response_price.status_code, 200)
        self.assertEqual(response_price_json, result_price)

    def test_find_pharm_num_mask_price_range(self):
        test_url = reverse('find_pharm_num_mask_price_range')
        test_data_more = {"low_price": 10,
                          "high_price": 30, "num": 2, "compare": "more"}
        test_data_less = {"low_price": 10,
                          "high_price": 30, "num": 2, "compare": "less"}
        result_more = ['Cash Saver Pharmacy', 'Drug Blend', 'Medlife',
                       'Thrifty Way Pharmacy', 'Longhorn Pharmacy',
                       'MedSavvy', 'Discount Drugs', 'Assured Rx']
        result_less = ['PharmaMed', 'Wellcare', 'Atlas Drugs', 'RxToMe',
                       'Pride Pharmacy', 'DFW Wellness', 'PrecisionMed']

        response_more = self.client.get(test_url, test_data_more)
        response_less = self.client.get(test_url, test_data_less)
        response_more_json = json.loads(response_more.content)[
            'num_of_mask_count_pharm_name']
        response_less_json = json.loads(response_less.content)[
            'num_of_mask_count_pharm_name']

        self.assertCountEqual(response_more_json, result_more)
        self.assertCountEqual(response_less_json, result_less)

    def test_find_user_date_range_top_total_amount(self):
        test_url = reverse('find_user_date_range_top_total_amount')
        test_data = {
            "low_day": "2021-01-27",
            "high_day": "2021-04-01",
            "num": 2}
        result_data = ["Connie Vasquez", "Ruby Andrews"]

        response = self.client.get(test_url, test_data)
        response_json = json.loads(response.content)['user_top_amount']

        self.assertEqual(response_json, result_data)

    def test_find_total_mask_num_dollar_date_range(self):
        test_url = reverse('find_total_mask_num_dollar_date_range')
        test_data = {"low_day": "2021-01-27", "high_day": "2021-04-01"}
        result_masks = {'total_masks': 11}
        result_mask_dollar = {'total_mask_dollar': 160.61}

        response = self.client.get(test_url, test_data)
        response_json_masks = json.loads(response.content)['total_masks']
        response_json_dollar = json.loads(
            response.content)['total_mask_dollar']

        self.assertEqual(response_json_masks, result_masks)
        self.assertEqual(response_json_dollar, result_mask_dollar)

    def test_search_pharm_mask_name(self):
        test_url = reverse('search_pharm_mask_name')
        test_pharm_data = {"search": "pharm", "query": "Med"}
        test_mask_data = {"search": "mask", "query": "Ma"}
        result_pharm = ["MedSavvy", "Medlife", "PrecisionMed", "PharmaMed"]
        result_mask = ["MaskT (black) (10 per pack)",
                       "Masquerade (blue) (6 per pack)",
                       "Masquerade (black) (3 per pack)",
                       "MaskT (blue) (3 per pack)",
                       "Masquerade (black) (10 per pack)",
                       "MaskT (black) (3 per pack)",
                       "Masquerade (black) (3 per pack)",
                       "MaskT (green) (10 per pack)",
                       "Masquerade (green) (10 per pack)",
                       "MaskT (green) (6 per pack)"]

        response_pharm = self.client.get(test_url, test_pharm_data)
        response_mask = self.client.get(test_url, test_mask_data)

        response_pharm_json = json.loads(response_pharm.content)['search']
        response_mask_json = json.loads(response_mask.content)['search']

        self.assertCountEqual(response_pharm_json, result_pharm)
        self.assertCountEqual(response_mask_json, result_mask)
