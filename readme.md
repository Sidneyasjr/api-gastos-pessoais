# Gerenciador de Gastos Pessoais

API criada com Flask



## Como Desenvolver?
1. Clone o repositório.
2. Crie um virtualenv com Python 3.9
3. Ative o virutalenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes

````console
git clone git@github.com:sidneyasjr/
cd api-gastos-pessoais
python -m venv .api-gastos-pessoais
source .api-gastos-pessoais/bin/activate
pip install -r requirements.txt
set FLASK_APP = 'app'
flask db init
flask db migrate
flask db upgrade
````



