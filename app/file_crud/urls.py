from django.urls import path

from .views import FileUploadDownloadAPIView, FileListAPIView

urlpatterns = [
    path(
        'upload_file/',
        FileUploadDownloadAPIView.as_view({'post': 'upload_file'}),
        name='upload_file'
    ),

    path(
        'delete_file/',
        FileUploadDownloadAPIView.as_view({'post': 'download_file'}),
        name='download_file'
    ),

    path(
        'list-file/',
        FileListAPIView.as_view(),
        name='file-list'
    ),
]
