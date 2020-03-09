import tempfile
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


def create_user(**params):
    """Helper to create users for our tests"""

    return get_user_model().objects.create_user(**params)


class PublicFileApiTestCase(TestCase):
    """Test public api for file"""

    def setUp(self):
        self.file_test_url = reverse('upload_file')
        self.client = APIClient()
        self.user = create_user(
            email='test@test.com',
            password='testpass',
            name='name'
        )

    def test_upload_legal_document_unauthorized(self):
        """Test uploading a legal document fails if unauthorized user"""

        response = self.client.put(self.file_test_url, {}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateFileApiTestCase(TestCase):
    """Test for private file api"""

    @staticmethod
    def _file_upload_url():
        """return document url to upload a file and attach to it"""
        return reverse('upload_file')

    @staticmethod
    def _file_delete_url():
        """return document url to upload a file and attach to it"""
        return reverse('delete_file')

    def setUp(self):
        self.client = APIClient()
        self.user = create_user(
            email='test@test.com',
            password='testpass',
            name='name'
        )
        self.client.force_authenticate(user=self.user)

    @patch('storages.backends.s3boto3.S3Boto3Storage.save')
    def test_upload_file_to_S3_AWS(self, mock_save):
        """Test for uploading a file and attach it to a legal document, state must change to waiting for review"""

        mock_save.return_value = 'test_txt.txt'

        with tempfile.NamedTemporaryFile(suffix='.txt') as ntf:
            ntf.write(b"Hello World")
            ntf.seek(0)

            document_url = self._file_upload_url()

            res = self.client.post(document_url, {'file': ntf}, multipart=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    @patch('storages.backends.s3boto3.S3Boto3Storage.save')
    def test_delete_file_to_S3_AWS(self, mock_save):
        """Test for uploading a file and attach it to a legal document, state must change to waiting for review"""

        mock_save.return_value = 'test_txt.txt'

        with tempfile.NamedTemporaryFile(suffix='.txt') as ntf:
            ntf.write(b"Hello World")
            ntf.seek(0)

            document_url = self._file_delete_url()

            res = self.client.post(document_url, {'file': ntf}, multipart=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_list_file_to_S3_AWS(self):
        url = reverse('file-list')

        res = self.client.get(url, format='json')
        response_data = res.json()
        print(response_data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
