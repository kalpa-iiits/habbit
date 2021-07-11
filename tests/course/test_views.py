import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestCourseList(APITestCase):
    @pytest.mark.django_db
    def test_can_get_course_list(self):
        url = reverse('course_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 8)
        

class TestWishlistList(APITestCase):
    @pytest.mark.django_db
    def test_can_get_wishlist_list(self):
        url = reverse('wishlist_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 8)