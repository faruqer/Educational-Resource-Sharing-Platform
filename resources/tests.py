from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Category, Resource


class ResourceModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='owner', password='pass12345')
        self.category = Category.objects.create(name='Mathematics', slug='mathematics')

    def test_resource_creation(self):
        resource = Resource.objects.create(
            title='Algebra Notes',
            description='Simple algebra notes',
            category=self.category,
            resource_type='pdf',
            external_url='https://example.com/algebra',
            created_by=self.user,
        )
        self.assertEqual(resource.title, 'Algebra Notes')
        self.assertEqual(str(resource), 'Algebra Notes')


class ResourceViewTests(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username='owner2', password='pass12345')
        self.other_user = User.objects.create_user(username='otheruser', password='pass12345')
        self.category = Category.objects.create(name='Science', slug='science')
        self.resource = Resource.objects.create(
            title='Physics Intro',
            description='A basic guide',
            category=self.category,
            resource_type='article',
            external_url='https://example.com/physics',
            created_by=self.owner,
        )

    def test_resource_list_page(self):
        response = self.client.get(reverse('resource_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Physics Intro')

    def test_resource_list_search_filter(self):
        response = self.client.get(reverse('resource_list'), {'q': 'Physics'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Physics Intro')

    def test_resource_create_requires_login(self):
        response = self.client.get(reverse('resource_create'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

    def test_owner_can_update_resource(self):
        self.client.login(username='owner2', password='pass12345')
        response = self.client.post(
            reverse('resource_update', kwargs={'pk': self.resource.pk}),
            {
                'title': 'Physics Intro Updated',
                'description': 'Updated description',
                'category': self.category.pk,
                'resource_type': 'article',
                'external_url': 'https://example.com/physics-new',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.resource.refresh_from_db()
        self.assertEqual(self.resource.title, 'Physics Intro Updated')

    def test_non_owner_cannot_update_resource(self):
        self.client.login(username='otheruser', password='pass12345')
        response = self.client.post(
            reverse('resource_update', kwargs={'pk': self.resource.pk}),
            {
                'title': 'Unauthorized Update',
                'description': 'Should fail',
                'category': self.category.pk,
                'resource_type': 'article',
                'external_url': 'https://example.com/fail',
            },
        )
        self.assertEqual(response.status_code, 403)

    def test_owner_can_delete_resource(self):
        self.client.login(username='owner2', password='pass12345')
        response = self.client.post(reverse('resource_delete', kwargs={'pk': self.resource.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Resource.objects.filter(pk=self.resource.pk).exists())
