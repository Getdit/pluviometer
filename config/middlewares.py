from django.http.response import HttpResponse


def verifications_middleware(get_response):

    def middleware(request):
        """Forcing the profile creation - This must be changed (for a redirect) when be useful that the user type more data for his profile"""
        user = request.user
        response = get_response(request)

        if user.is_anonymous == False and not user.is_superuser:

            if ((not user.profile.projects) or user.profile.is_researcher):
                return HttpResponse('Opa, seu acesso não foi liberado.')

        return response

    return middleware