
#!/usr/bin/env python
import sys
import os
sys.path.append(os.path.abspath("../opencv_django_demo"))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "opencv_site.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
