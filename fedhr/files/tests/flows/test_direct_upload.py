from django.test import TestCase

from fedhr.files.tests.factories import FileFactory


class DirectUploadApiTests(TestCase):
    def test_direct_file_upload(self):
        file = FileFactory.build()
        print('file: ', file.__dict__)
    """
    We want to test the following:

    1. A start-upload-finish cycle, where we patch the presign generation with local upload storage.
    """
