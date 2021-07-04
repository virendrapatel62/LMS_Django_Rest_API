from django.core.wsgi import get_wsgi_application
import os
import sys
sys.path.append('/opt/bitnami/projects/feelfreetocode')
os.environ.setdefault("PYTHON_EGG_CACHE",
                      "/opt/bitnami/projects/feelfreetocode/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "feelfreetocode.settings")
application = get_wsgi_application()
