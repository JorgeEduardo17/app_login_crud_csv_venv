import os

from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import File

AWS_S3_BUCKET_ID = os.environ.get('AWS_S3_BUCKET_ID', '')

from .helpers.file_crud_helpers import upload_file, download_file
from .serializers import FileSerializer


class FileUploadDownloadAPIView(viewsets.ModelViewSet):
    """View for legal document"""
    queryset = File.objects.all()
    name = 'upload_file'
    permission_classes = (IsAuthenticated,)

    @action(methods=['POST'], detail=True)
    def upload_file(self, request):
        """Upload an file to a legal_document"""
        request = self.request
        file = request.FILES('file')

        confirmation = upload_file(file, AWS_S3_BUCKET_ID)
        if confirmation:
            return Response({'Succesfully upload_file'}, status.HTTP_200_OK)
        else:
            return Response({'failled upload_file'}, status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=True)
    def download_file(self, request):
        """download a legal_document file"""
        request = self.request
        file = request.FILES('file')

        confirmation = download_file(file, AWS_S3_BUCKET_ID)
        if confirmation:
            return Response({'Succesfully download'}, status.HTTP_200_OK)
        else:
            return Response({'failled upload_file'}, status.HTTP_400_BAD_REQUEST)


class FileListAPIView(generics.ListAPIView):
    name = 'file-list'
    serializer_class = FileSerializer
    permission_classes = (IsAuthenticated,)
    queryset = File.objects.all()
    ordering = ['-uploaded_at']

