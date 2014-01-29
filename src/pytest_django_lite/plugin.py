import os
import pytest

try:
    from django.conf import settings
except ImportError:
    settings = None  # NOQA


def is_configured():
    if settings is None:
        return False
    return settings.configured or os.environ.get('DJANGO_SETTINGS_MODULE')


@pytest.fixture(autouse=True, scope='session')
def _django_runner(request):
    if not is_configured():
        return

    from django.test.simple import DjangoTestSuiteRunner

    import django
    if hasattr(django, 'setup'):
        django.setup()

    runner = DjangoTestSuiteRunner(interactive=False)
    runner.setup_test_environment()
    request.addfinalizer(runner.teardown_test_environment)

    config = runner.setup_databases()

    def teardown_database():
        runner.teardown_databases(config)
    request.addfinalizer(teardown_database)

    return runner
