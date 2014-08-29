Introdução
==========

Pretende-se com esta proposta de pesquisa investigar e elaborar aplicações em
tempo real, para a internet, utilizando a linguagem JavaScript no servidor
Node.Js. 

Atualmente a internet tem crescido mais depressa que o rádio e a televisão.
Hoje a Internet, como mídia de comunicação, tem o mais amplo de todos os
alcances do que as mídias citadas anteriormente, conforme pode ser visto na
pesquisa do IBGE de 2005 para 2011, número de internautas cresce 143.8% e o de
pessoas com celular, 107.2%. E para continuar a oferecer serviços e
informações, com rapidez e até mesmo em tempo real, é necessário se preocupar
com a quantidade de milhões de usuários simultâneos, que cresce
exponencialmente, e vencer barreiras tecnológicas de escalabilidade e
desempenho nos servidores.

Segundo TILKOV (2010), para resolver problemas de que lidam com múltiplas
entradas e saídas (E/S), como manipular múltiplas requisições de clientes em
servidores, os programadores adotaram utilizar técnicas de programação
multithread (processamento simultâneo de um conjunto de tarefas), ou técnicas
de programação paralela, dividindo o processamento da aplicação em vários
núcleos dos processadores da CPU ou até mesmo utilizando computação
distribuída. Este modelo de programação para atender múltiplas entradas e
saídas é fácil de entender, implementar e permite executar os processos de
forma rápida e eficiente. Porém este modelo apresenta algumas falhas, por
exemplo, quando uma thread (conjunto de tarefas) consome um recurso X de
processamento ou operação de entrada e saída e em seguida o aplicativo executa
uma nova thread (conjunto de tarefas) que necessita consumir este mesmo
recurso, teremos um bloqueio o qual é necessário esperar a primeira thread
(conjunto de tarefas) terminar sua execução, liberar o recurso e então
prosseguir com o processamento da segunda thread. Como dito por TILKOV mesmo
que muitos tenham obtido sucesso em usar multithread (processamento simultâneo
de um conjunto de tarefas)  em aplicações, não é fácil isolar e corrigir
problemas como bloqueios e falhas, proteger recursos compartilhados entre as
threads (conjunto de tarefas). Também perde-se o controle quando ocorre o
desenvolvimento multithreading (processamento simultâneo de um conjunto de
tarefas) pois o sistema operacional é responsável por decidir qual thread
(conjunto de tarefas) será executada e por quanto tempo. (TILKOV, 2010, p.80)

Em sistemas web desenvolvidos sob as plataformas tradicionais como JAVA, PHP,
.NET  dentre outros é necessário paralisar um processamento enquanto utiliza
uma entrada e saída do servidor. Essa paralisação é conhecida como um modelo
bloqueante. Exemplificando este modelo, em um servidor Web que cada processo é
uma requisição de feita pelo usuário. Com o decorrer novos usuários realizam
novas requisições aumentando o processamento. No modelo bloqueante cada
requisição é enfileirada e depois processadas uma a uma. Enquanto uma
requisição esta sendo processada as demais ficam em espera, mantendo-se ociosas
por um período  indeterminado na fila. (PEREIRA, 2013)
Com esta arquitetura tradicional, gasta-se muito tempo mantendo uma fila de
espera com processos ociosos, tais como: envio de e-mails, consultas em banco
de dados, leitura em disco que não liberam recursos enquanto não forem
finalizadas. Com o aumento dos acessos ao sistema é necessário fazer uma
atualização do hardware (equipamento). (PEREIRA, 2013).
De acordo com Abernethy (2011), explica que em linguagens como Java e PHP, cada
conexão cria-se uma nova thread ( conjunto de tarefas ) com 2 MB de memória
RAM. Se em um servidor possuir 8 GigaBytes de memória RAM, teoricamente o número
máximo de conexões concorrentes é aproximadamente 4.000 usuários. Com o
aumento da base de cliente, e claro, se quiser que o aplicativo web suporte
mais usuários, é necessário adicionar mais e mais servidores. Somando aos
custos de adição de novos equipamentos, ha possíveis problemas técnicos que
devem ser considerados tal como o um usuário usar diferentes servidores para
cada requisição, portanto, os recursos devem estar compartilhados em todos os
servidores. Por todas essas razões, o gargalo em toda a arquitetura da
aplicação web ( incluindo a velocidade de tráfego, velocidade do processador e
velocidade da memória RAM) estaria associado ao número máximo de conexões
concorrentes que um servidor pode manipular.
Portanto, observa-se que o escalonamento horizontal, adicionando novos
servidores, além do custo altíssimo, torna a arquitetura do sistema complexa
pois será necessário acrescentar servidores de balanceamento, rede estruturada
da central de dados que seja capaz de suportar um alto tráfego e acompanhamento
dos processos do sistema de perto para que os bloqueios sejam consertados em
tempo hábil. A utilização de escalonamento vertical, ou melhor, atualização de
hardware – colocando mais processadores ou memória - pode inviabilizar a
arquitetura do sistema, visto que ha uma barreira de hardware, mais
especificamente, placas-mãe que não suportam mais de 8 *slots* de memória ou
determinados modelos de memória RAM, suporte a processadores com mais de 7
núcleos. Além dessas limitações tecnológicas, ha o agravante do alto  custo
para atualizar este hardware. Processadores com 7 núcleos são caros e
dependendo dos casos é necessário trocar todo o equipamento – hardware - para
garantir o devido funcionamento dos componentes.
Pelos problemas citados acima surge a necessidade de resolver este problema, em
nível de software, que permita receber um grande número de conexões simultâneas
nos servidores, capaz de ser escalável e consumir menores índices de memória
RAM. Um paradigma adotado para esta solução é a programação orientada a
eventos, onde tudo gira em torno de eventos, indicando que exite um produtor do
evento e um consumidor daquele evento. (Junior, 2012)
O JavaScript, linguagem de programação, fornece o modelo de eventos
assíncronos, funções anônimas e callbacks.  Como JUNIOR  exemplificou, um
programa assíncrono ao fazer uma requisição a um banco de dados especifica o
que deve ser feito com os resultados do banco de dados. Este programa não
espera a finalização da requisição e processa outras atividades. Apenas
quando o resultado da requisição é retornado do banco de dados, a codificação
para manipular os estes dados é executado. A esta lógica de programação,
executada após a fim da requisição, dá-se ao nome de callback. (JUNIOR, 2012,
p.2)
A partir dessa necessidade surge o ambiente de desenvolvimento Node.Js, que é
melhor descrito por JUNIOR (2012) como uma plataforma cujo o objetivo é a fácil
construção de rápidas e escaláveis aplicações de rede. Para isto o Node.Js
emprega orientação a eventos utilizando o JavaScript Engine V8 do Google,
operações de entradas e saídas em eventos (assíncronos) e não bloqueantes.
Abenerthy cita que ao invés de criar novas threads (conjunto de tarefas) no
sistema operacional para cada conexão e alocar a memória RAM que acompanha
essas threads (conjunto de tarefas), cada conexão dispara um evento executado
no processo do motor Node.Js. O Node.Js afirma que ele nunca irá ter bloqueios
ou impasses, já que bloqueios não é uma característica da sua plataforma mesmo
em processamento de entradas e saídas.. Node.Js afirma que um servidor pode
suportar dezenas de milhares de conexões simultâneas. (ABENERTHY, 2011).
Por fim, busca-se com o Node.Js, o qual será a base para esta proposta de
pesquisa, demonstrar uma aplicação Web capaz de mostrar, em tempo real, a
localização de dispositivos móveis através das coordenadas de latitude e
longitude utilizando o paradigma de orientação a eventos, com alta concorrência
de conexões. 


Motivação
---------

Com a chegada de aplicativos web integrados a dispositivos móveis há a
necessidade de se ter uma arquitetura capaz de suportar milhares de usuários e
que ela atenda a todos os graus de satisfação deles. No repositório do Node.Js
possui uma lista de projetos, aplicações e empresas que utilizam o Node.Js.
Dentre estes items pode-se destacar duas empresas, o LinkdIn que utiliza o
ambiente Node.JS para aplicações móveis e o PayPal famoso *gateway* - ponte - de
pagamento.


Objetivos
---------

Objetivo Geral
^^^^^^^^^^^^^^

Pretende-se com esta pesquisa investigar, comparar e demonstrar a capacidade do
ambiente Node.Js de processar e responder milhares de requisições comparando-o
com um ambiente  Python. 

Para isso tem-se dois aplicativos desenvolvidos como uma API RESTFul provendo as 
operações básicas como Criar, Atualizar, Listar e Deletar de uma lista de contatos.


De antemão não será desenvolviedo um sistema complexo como os já
existentes no mercado.


Objetivos específicos
^^^^^^^^^^^^^^^^^^^^^

Os objetivos específicos deste trabalho são:

* Estudo sobre ambiente de desenvolvimento Node.Js
* Apresentar a metodologia de desenvolvimento da arquitetura REST em Node.Js;
* Utilização do protótipo desenvolvido.
* Testes de cargas em aplicações web.
* Apresentar os resultados alcançados através dos testes realizados.

Problema
--------

No cenário atual, em termos de desenvolvimento web com as linguagens de programação tradicionais,
para garantirmos disponibilidade das informações a milhares de usuário é necessário um conjunto de ferramentas e técnicas.
Como exemplo tem-se o vídeo da palestra  Usando Django para atender 12 milhões de usuários apresentada
por Rômulo Jales e Victor Pantoja no evento da Python Brasil 9.
Nesta palestra foi apresentada a arquitetura utilizada pelo portal Globo Esporte [#]_
utilizando várias técnicas para ganhar desempenho, tais como, servir páginas HTML estáticas através do NGINX [#]_,
gravar as páginas geradas em disco, utilizar SSI [#]_ ao invés de chamadas Ajax [#]_,
ter um sistema de cache de objeto distribuído em memória como o Memcached e um acelerador de aplicações web cache HTTP
e proxy reverso tal como Varnish, minificar arquivos CSS e JavaScript, utilizar CSS Sprite,
utilizar compactação nos arquivos servidos através de, dentre outras técnicas. 

Para alcançar este número de usuários suportados no portal é necessário ter uma equipe
capacitada para realizar técnicas de programação eficazes, analise e configuração de
ferramentas de cache disponíveis no mercado e uma central de dados capacitada.
O custo para manter esse eco sistema funcionando, provavelmente é alto.

Mediante a esta análise surge a proposta de utilizar o ambiente de programação Node.Js para comprovar 
sua capacidade de aceitar milhares requisições de usuários utilizando o paradigma de programação orientada a eventos no servidor.


Organização da monografia
-------------------------

.. warning::
    
    Corrigir os capítulos


Para contextualizar o leitor, o capítulo três, documenta a lista de requisitos base do aplicativo. O capitulo quatro aborda o referencial teórico e fontes de estudos utilizados para iniciar com o ambiente Node.Js. Já o capítulo cinco apresenta os aplicativos desenvolvidos.  O capitulo seis descreve os testes realizados e os resultados obtidos. Por fim, o capitulo sete, conclui o trabalho acadêmico.


.. rubric:: Notas de rodapé

.. [#] Sítio www.globoesporte.com.br 
.. [#] Nginx [engine x] é um servidor HTTP e proxy reverso
.. [#] SSI são diretivas que são colocadas em páginas HTML, enquanto as páginas estão sendo servidas
.. [#] Ajax Javasvript assíncrono e xml, utilizado para atualizar partes da página web sem recarrega-la
