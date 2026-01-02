from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class BearerAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None

        try:
            prefix, token = auth_header.split()
            if prefix.lower() != 'bearer':
                raise ValueError("Invalid token prefix")
        except ValueError as e:
            raise AuthenticationFailed(f"Invalid Authorization header: {e}")

        # This is a simple hardcoded token for demonstration purposes.
        # In a real application, you would validate the token against a database.
        valid_token = "d33b060b880252300919882e73261681b87f9286"

        if token != valid_token:
            raise AuthenticationFailed("Invalid token")

        return (None, None)  # No user, just authenticated
