from django.http.response import HttpResponse
from accounts.models import Profile
#import AnonymouseUser
from django.contrib.auth.models import AnonymousUser

def verifications_middleware(get_response):

    def middleware(request):
        """Forcing the profile creation - This must be changed (for a redirect) when be useful that the user type more data for his profile"""
        user = request.user
        response = get_response(request)

        if not (user.is_anonymous or Profile.objects.filter(owner=user).exists()):
            Profile.objects.create(owner=user)

        if user.is_anonymous == False and not user.is_superuser:
            if (not user.profile.active) or ((not user.profile.projects) or user.profile.is_researcher):
                return HttpResponse('Opa, seu acesso não foi liberado.')
        return response

    return middleware