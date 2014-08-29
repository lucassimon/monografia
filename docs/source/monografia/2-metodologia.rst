Metodologia
===========

Baseando-se em metodologias de desenvolvimento de software ágil Scrum, foram desenvolvidas as seguintes etapas para elaboração deste trabalho:

Etapas
------

Levantamento de requisitos
^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Estudar a arquitetura web** 
  Buscando um entendimento básico de como é a implementação de uma aplicação RESTful e seus protocolos relacionados ao HTTP.

* **Realizar levantamentos de requisitos da aplicação**
  Coletar funcionalidades necessárias para realizar a aplicação independente da plataforma de desenvolvimento utilizada.

* **Especificar serviços da aplicação**
  Detalhar e documentar o serviço de hospedagem na internet, além de outros componentes necessários para o funcionamento do ecossistema da aplicação como:
    * Hardware utilizado;
    * Servidor web para responder requisições na porta 80;
    * Serviços adicionais instalados ( Banco de dados );
    * Softwares para monitorar desempenho e utilização do servidor;

Estudo do ambiente de programação Node.Js
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Estudar o paradigma de orientação a eventos**

* **Estudar o Event Loop**
  Busca um entendimento básico sobre o ciclo de eventos (Event-Loop) e como ele é utilizado no NodeJs.

* **Estudar as principais características do Node.Js**
  Conhecer o modelo *single-thread*, diferenças entre o modelo assíncrono e síncrono, dentre outros.

* **Estudo do framework Express**
  Conhecer o framework feito em Node.Js que será a base para criar a aplicação devido a grandes módulos já inclusos e 
  se codificar de maneira RESTful.

Criar dois aplicativos em diferentes paradigmas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Desenvolvimento da aplicação no paradigma orientado a eventos**
  Desenvolver  um aplicativo escrito no ambiente Node.Js com o framework Express.Js

* **Desenvolvimento do mesmo aplicativo em outros ambientes**
  Busca-se com esta etapa ter um aplicativo escrito na linguagem Python com o framework Django para comparamos o desempenho,
  do ambiente aqui estudado.

Especificar testes e comparar os resultados 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Utilizar testes de carga nas API's**
  Realizar um teste de carga utilizando os serviços web como o loader.io e blitz.io

* **Descrever o software de testes de carga**
  Descrever passo a passo como gerar um teste de carga na aplicação dos serviços descritos acima.

* **Executar os testes para avaliar o desempenho das aplicações**
  Executar os testes para obter informações e medir o desempenho de cada aplicação.
  
* **Avaliar os resultados obtidos após a analise, coleta e definições das métricas**
  Por último realizar uma análise sobre o desempenho positivo ou negativo de cada modelo desenvolvido.
