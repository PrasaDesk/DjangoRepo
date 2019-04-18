from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user_name):
    refresh = RefreshToken.for_user(user_name)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
