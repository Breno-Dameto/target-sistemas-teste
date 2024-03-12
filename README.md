# Desafio Estágio Target Sistemas

# Resolução
Resolução dos exercicios propostos no processo seletivo para o Estágio em Desenvolvimento na empresa Target Sistemas.

# Tecnologias utilizadas
- Python

# Exercicios:
1) Observe o trecho de código abaixo:
   

      int INDICE = 13, SOMA = 0, K = 0;
      
      enquanto K < INDICE faça  
      
      {  
      
      K = K + 1;  
      
      SOMA = SOMA + K;  
      
      }  
      
      imprimir(SOMA);  



Ao final do processamento, qual será o valor da variável SOMA?

[Resolução Exercicio 1](https://github.com/Breno-Dameto/target-sistemas-teste/tree/e6f553ca423e9a8ae39dc422b4e501cb46684195/exercicio1) = 91

2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

[Resolução Exercicio 2](https://github.com/Breno-Dameto/target-sistemas-teste/tree/e6f553ca423e9a8ae39dc422b4e501cb46684195/exercicio2)

3) Descubra a lógica e complete o próximo elemento:

    a) 1, 3, 5, 7, <strong><code>9</code></strong>
     ```
     R: A lógica da sequência "a" consiste em adicionar 2 ao número anterior;
     então, o próximo número é 9 = 7 + 2.
     ```
    b) 2, 4, 8, 16, 32, 64, <strong><code>128</code></strong>
     ```
     R: A lógica da sequência "b" é multiplicar cada número por 2;
     sendo assim, o próximo número é 128 = 64 * 2.

     ```
    
    c) 0, 1, 4, 9, 16, 25, 36, <strong><code>49</code></strong>
     ```
     R: A lógica da sequência "c" é a representação dos quadrados dos números naturais;
     o próximo número é 49 = 7².
     ```
    
    d) 4, 16, 36, 64, <strong><code>100</code></strong>
     ```
     R: A lógica da sequência "d" é a representação dos quadrados dos números pares;
     o próximo número é 100 = 10².
     ```
    
    e) 1, 1, 2, 3, 5, 8,  <strong><code>13</code></strong>
     ```
     R: A lógica da sequência "e" é a representação da sequência de Fibonacci, vista no exercício anterior;
     em que cada número é a soma dos dois anteriores; o próximo número é 13 = 5 + 8.
     ```
    
    f) 2,10, 12, 16, 17, 18, 19, <strong><code>200</code></strong>
     ```
     R: A lógica da sequência "f" consiste em números naturais com a inicial 'D';
     portanto, o próximo número é 200.
     ```

4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

    Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

   ```
   1. Ligaria o interruptor e aguardaria alguns minutos.
   2. Depois de alguns minutos, desligaria o primeiro interuptor e ligaria o segundo.
   3. Agora entraria na sala onde as lâmpadas estão e iria observar:
       A lampada que estiver acesa pertence ao segundo interruptor que foi ligado.
       Caso ela esteja apagada, mas esteja quente. O interruptor que foi ligado primeiro controla essa lâmpada.
       Se por acaso ela estiver fria, então é o terceiro interruptor que não foi ligado que controla essa lâmpada
   ```
5) Escreva um programa que inverta os caracteres de um string.


    IMPORTANTE:
    
    a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
    
    b) Evite usar funções prontas, como, por exemplo, reverse;

   [Resolução Exercicio 5](https://github.com/Breno-Dameto/target-sistemas-teste/tree/e6f553ca423e9a8ae39dc422b4e501cb46684195/exercicio5)
 
