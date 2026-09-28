from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import X


class XModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="StrongPassword123!",
        )

    def test_create_post(self):
        post = X.objects.create(
            user=self.user,
            text="Hello from XMini!",
        )

        self.assertEqual(post.user, self.user)
        self.assertEqual(post.text, "Hello from XMini!")

    def test_post_string_representation(self):
        post = X.objects.create(
            user=self.user,
            text="Hello world",
        )

        self.assertEqual(
            str(post),
            "testuser - Hello world",
        )


class XViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="StrongPassword123!",
        )

        self.other_user = User.objects.create_user(
            username="otheruser",
            email="other@example.com",
            password="StrongPassword123!",
        )

        self.post = X.objects.create(
            user=self.user,
            text="My first post",
        )

    def test_post_list_is_accessible(self):
        response = self.client.get(
            reverse("x_list")
        )

        self.assertEqual(response.status_code, 200)

    def test_search_finds_post(self):
        response = self.client.get(
            reverse("x_list"),
            {"q": "first"},
        )

        self.assertContains(
            response,
            "My first post",
        )

    def test_search_by_username(self):
        response = self.client.get(
            reverse("x_list"),
            {"q": "testuser"},
        )

        self.assertContains(
            response,
            "My first post",
        )

    def test_create_requires_login(self):
        response = self.client.get(
            reverse("x_create")
        )

        self.assertEqual(
            response.status_code,
            302,
        )

    def test_logged_in_user_can_create_post(self):
        self.client.login(
            username="testuser",
            password="StrongPassword123!",
        )

        response = self.client.post(
            reverse("x_create"),
            {
                "text": "A new post",
            },
        )

        self.assertRedirects(
            response,
            reverse("x_list"),
        )

        self.assertTrue(
            X.objects.filter(
                text="A new post",
                user=self.user,
            ).exists()
        )

    def test_user_can_edit_own_post(self):
        self.client.login(
            username="testuser",
            password="StrongPassword123!",
        )

        response = self.client.post(
            reverse(
                "x_edit",
                args=[self.post.pk],
            ),
            {
                "text": "Updated post",
            },
        )

        self.assertRedirects(
            response,
            reverse("x_list"),
        )

        self.post.refresh_from_db()

        self.assertEqual(
            self.post.text,
            "Updated post",
        )

    def test_user_cannot_edit_other_users_post(self):
        self.client.login(
            username="otheruser",
            password="StrongPassword123!",
        )

        response = self.client.get(
            reverse(
                "x_edit",
                args=[self.post.pk],
            )
        )

        self.assertEqual(
            response.status_code,
            404,
        )

    def test_user_can_delete_own_post(self):
        self.client.login(
            username="testuser",
            password="StrongPassword123!",
        )

        response = self.client.post(
            reverse(
                "x_delete",
                args=[self.post.pk],
            )
        )

        self.assertRedirects(
            response,
            reverse("x_list"),
        )

        self.assertFalse(
            X.objects.filter(
                pk=self.post.pk
            ).exists()
        )

    def test_user_cannot_delete_other_users_post(self):
        self.client.login(
            username="otheruser",
            password="StrongPassword123!",
        )

        response = self.client.post(
            reverse(
                "x_delete",
                args=[self.post.pk],
            )
        )

        self.assertEqual(
            response.status_code,
            404,
        )

        self.assertTrue(
            X.objects.filter(
                pk=self.post.pk
            ).exists()
        )

    def test_profile_page(self):
        response = self.client.get(
            reverse(
                "user_profile",
                args=[self.user.username],
            )
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertContains(
            response,
            "@testuser",
        )