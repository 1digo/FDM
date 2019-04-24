from split_settings.tools import include, optional

include(
    'components/django.py',
    'components/rest_framework.py',
    'components/rest_framework_swagger.py',
    optional('local_settings.py'),
)
