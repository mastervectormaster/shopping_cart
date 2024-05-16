from rest_framework_simplejwt.authentication import JWTAuthentication
JWT_authenticator = JWTAuthentication()

def get_user_email_from_request(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Check if the user has an email attribute
        if hasattr(request.user, 'email'):
            # Return the email
            return request.user.email
        else:
            # If the user doesn't have an email attribute, return None
            return None
    else:
        # If the user is not authenticated, return None
        return None

