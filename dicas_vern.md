# MANIPULANDO VIRTUAL ENVIROMENT

## DEFINIÇÃO
VENV OU VIRTUAL ENVIROMENT É EQUIVALENTE A UM CONTEINER OU DOCKER

## DINAMICA TRABALHO

1) Criar uma venv 

python -m venv venv

2) Ativar uma venv 

Windows: C:\XXX>venv\Scripts\activate (não pode ser no powershell)

Unix: Source venv/bin/activate

3) instalar ou configurar tecnologias 

python -m pip install pandas

4) Depois de criar, instalar, atualizar e configurar a venv, é necessário criar o arquivo requirements.txt

python -m pip freeze > requirements.txt

5) Toda a vez que o repositório for clonado (usado pela primeira vez), é necessário:
    a) criar e a ativar a venv
    b) instalar os pacotes que estão no arquivo requirements.txt
        python -m pip install -r requirements.txt

6) Se for trocar de projeto  cuidar para desativar a venv

deactivate
