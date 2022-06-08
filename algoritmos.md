# Algotimos

Sequencia de Instruções lógicas que visam obter a solução de um problema.

Problema: ir a padaria e comprar pão.
Premissa: Padaria da esquina abre até 12h, semana até 19h, feriado (exceto Natal) não abre.

1. A padaria está aberta?
	1. Se é feriado e NÃO é natal: não
	2. Senão, Se é sábado OU domingo E antes do meio dia: sim
	3. Senão, se é dia de semana E antes das 19h: sim
	4. senão: não
2. Se padaria está aberta E:
	1. Se está chovendo: Pegar guarda-chuvas
	2. Se está chovendo E calor: Pegar guarda-chuvas e garrafa de agua
	3. Se está chovendo E frio OU nevando: pegar guarda chuva, blusa e botas
	4. Ir até a padaria:
		1. Se tem pao integral E baguete: Pedir 6 de cada
		2. Senão, se tem apenas pao integral OU baguete: Pedir 12
		3. Senão: Pedir 6 de qualquer pão
3. Senão
	1. Ficar em casa em comer bolachas

Levando Isso para o código: 
- Se -> if
- Senão, se -> elif (else if)
- Senão -> else

Operadores Lógicos
- E -> and
- OU -> or
- Não -> not

Assignments
- A padaria está aberta? 
Variavel com true | false

Expressions
- É feriado? -> bool True, False
- É natal?
- É feriado E não é natal?
- É sabado OU é domingo?

Actions
funcao / metodo / instrução
- checar qual é o dia atual
- pegar
- ficar em casa

