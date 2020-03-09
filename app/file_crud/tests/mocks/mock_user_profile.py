from django.contrib.auth import get_user_model

# Mock Parameters
mock_first_name = 'Jorge'


def mock_user_profile(email="test@tests.com"):
    User = get_user_model()
    user = User(
        name=mock_first_name,
        email=email,
    )
    return user
