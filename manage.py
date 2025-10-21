#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestao_acai.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django..."
        ) from exc

    # --- APLICA MIGRAÇÕES AUTOMATICAMENTE NO DEPLOY ---
    import django
    django.setup()
    from django.core.management import call_command
    print("🚀 Aplicando migrações...")
    call_command('migrate', interactive=False)

    # --- CRIA SUPERUSER AUTOMATICAMENTE (SE VARIÁVEL SETADA) ---
    from django.contrib.auth import get_user_model
    if os.environ.get("CREATE_SUPERUSER", "False") == "True":
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            print("⚙️ Criando superusuário admin automaticamente...")
            User.objects.create_superuser(username="admin", password="123", email="")
        else:
            print("✅ Superusuário já existe.")

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
