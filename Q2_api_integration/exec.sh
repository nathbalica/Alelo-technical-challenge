#!/bin/bash

env_name=$1
port=$2

if [ -e "$env_name" ]; then
	rm -rf $env_name
fi

python3 -m venv $env_name
echo "Subindo o ambiente virtual"
echo "Ativando o ambiente virutal 'alelo-venv'"
source $env_name/bin/activate
echo "Instalando Bibliotecas e Dependencias"
pip install -r requirements.txt > /dev/null
echo "Bibliotecas e Dependecias instaladas com Suceso!!"
echo "Executando a API de integração na porta $port"
python3 app.py -p $port
