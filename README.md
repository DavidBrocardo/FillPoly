# FillPoly

TRABALHO 1 DE COMPUTAÇÃO GRÁFICA – TURMA 2024 

O algoritmo fillpoly identifica quais scanlines devem ser processadas,
registrando todas as interseções entre elas e as arestas que compõem a fronteira do
polígono. 

Neste trabalho o que se pede é a implementação de um software que seja
capaz de desenhar e pintar a região interna de polígonos (algoritmo fillpoly). Os requisitos
são:
1) O algoritmo a ser implementado deve usar aritmética incremental (requisito
obrigatório), conforme orientações apresentadas em sala de aula;
2) Pode ser desenhando qualquer tipo de polígono (convexo, côncavo ou com
autointerseção);
3) O usuário pode desenhar um ou mais polígonos de qualquer formato na tela
do computador, usando para isso cliques do mouse;
4) Cada polígono pode ser selecionado individualmente pelo usuário, usando
para isso cliques do mouse sobre a interface onde estão desenhados;
5) O usuário pode selecionar um polígono e trocar a cor de preenchimento
(requisito obrigatório);
6) Definida a geometria do polígono e sua cor de preenchimento deve-se pintar
apenas os pixels que pertençam à região interna do polígono (requisito
obrigatório);
7) Deve estar disponível ao usuário a opção de pintar ou não pintar as arestas
dos polígonos. Neste caso a cor das arestas será sempre fixa (em amarelo);
8) Polígonos selecionados podem ser excluídos da lista de polígonos
manipuladas pelo software.
