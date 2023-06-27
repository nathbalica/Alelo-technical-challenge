algoritmo "exercicio_1"
// 
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 6/26/2023
Var
   // Adição da declaracao da variavel soma
   numero1, numero2, soma: inteiro
   
Iniciol
   escreva("Digite o primeiro número: ")
   leia(numero1)

   escreva("Digite o segundo número: ")
   leia(numero2)
   //Substituiu o operador = por <- para atribuir o valor da
   //soma das variáveis numero1 e numero2 à variável soma.
   soma <- numero1 + numero2

   se soma > 10 entao
     //Mudou a chamada de função escrevaL para escrevaL.
     //A função escrevaL é usada para escrever uma linha
     //com quebra de linha ao final.
     escrevaL("A soma é maior que 10")

   senao
     escrevaL("A soma é menor ou igual a 10!")
   //Incluiu o comando fimse para encerrar o bloco condicional se-senão.
   fimse
   
   // Mudou a concatenação da string para incluir
   //diretamente a variável soma utilizando a vírgula.

   escreva("O resultado da soma é: ",soma)

//Mudou a palavra-chave fim_algoritmo para Fimalgoritmo para indicar o fim do algoritmo.
Fimalgoritmo


## Exercicio 2

### Instalacao das libs
  ´´´
    ./install.sh
    python3 -m venv alelo-venv
    source alelo-venv/bin/activate
    pip install -r requirements.txt
    python app.py
  ´´´