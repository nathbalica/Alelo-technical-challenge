algoritmo "exercicio_1"

Var
   // Declaração da variável soma para armazenar a soma dos números
   numero1, numero2, soma: inteiro
   
Inicio
   escreva("Digite o primeiro número: ")
   leia(numero1)

   escreva("Digite o segundo número: ")
   leia(numero2)
   
   // Calcula a soma dos números e atribui o resultado à variável soma
   soma <- numero1 + numero2

   se soma > 10 entao
     // Exibe uma mensagem indicando que a soma é maior que 10
     escrevaL("A soma é maior que 10")
   senao
     // Exibe uma mensagem indicando que a soma é menor ou igual a 10
     escrevaL("A soma é menor ou igual a 10!")
   fimse
   
   // Exibe o resultado da soma
   escreva("O resultado da soma é: ", soma)

// Fim do algoritmo
Fimalgoritmo
