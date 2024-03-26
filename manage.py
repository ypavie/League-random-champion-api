#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import requests
import json


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lor_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # response = requests.get('https://ddragon.leagueoflegends.com/api/versions.json')
    # CURRENT_PATCH = json.loads(response.text)[0]
    # response = requests.get(f'https://ddragon.leagueoflegends.com/cdn/14.6.1/data/en_US/item.json')
    # items = json.loads(response.text)
    # with open(f'lor_backend/assets/items_14.6.1.json', 'w') as items_file:
    #     json.dump(items, items_file)
    main()
