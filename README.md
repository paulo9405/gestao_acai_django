Python 3.9.6

1 - Clonar o projeto do GitHub.

2 - Cria o ambiente de trabalho e ativa ele.

3 - Instala os requirements 'pip install -r requirements-dev.txt'

- cria uma pasta .env na raiz do projeto e gera uma secrete key
    comando: python -c "from django.core.management.utils import get_random_secret_key;       
    print(get_random_secret_key())"
    dentro do arquivo .env cria a variavel:
    SECRET_KEY=secret key aqui

4 - Faz as migrações do db

5 - Cria o usuariosuperuser

6 - Roda o sistema 'runserver'

7 - Acessa o sistema "http://localhost:8000/"
