from django.conf import settings


def global_variables(request):
    try:
        context = {
            'company_info': settings.COMPANY_INFO
        }
    except AttributeError:
        context = {
            'company_info': {
                "address": "123",
                "phone": "+9312312213",
                "email": "example.com",
            }

        }

    return context
