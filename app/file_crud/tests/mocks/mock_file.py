from uuid import uuid4

from ...models import File


def mock_user_profile(name='test'):
    file = File(
        uuid=uuid4,
        name='test_file',
        explanation='test backend',
    )
    file.save()
    return file
