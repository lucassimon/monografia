Protótipo
=========

Este capítulo descreve como foram desenvolvidos os protótipos e abordagens adotadas para a API RESTFul.

Neste protótipo o aplicativo tem como objetivo principal realizar operações de CRUD para um recurso chamado **Contatos**.

Toda a especificação do protótipo se encontra nos apêndices I, II, sendo que para compreender este capítulo é necessário a leitura prévia destes documentos.


Desenvolvimento dos Protótipos
------------------------------

Primeiramente é necessário informar que foram desenvolvidos dois protótipos,
ambos possuem as mesmas funções, porém, cada um aborda de maneira distinta 
as tecnologias utilizadas.

O ciclo de vida do protótipo iniciou pela concepção, onde foram organizados
algumas idéias e posteriormente foi escutado a opnião de algumas pessoas,
logo, o conceito da API RESTFul para analise de desempenho foi definido e 
iniciou-se a etapa da pré-produção, onde foram elaborados os documentos
Apêndice I e Apêndice II.

A etapa de produção foi iniciada logo após os documentos estarem com todos 
os requisitos mínimos definidos, nessa etapa, foi criado um projeto no ambiente Node.Js e Express.Js, onde foi implementado uma simples API RESTFul responsável pelas operações de CRUD do recurso de Contatos.

Nas próximas seções são descritos o desenvolvimento de cada protótipo.

Desenvolvimento da API em Node
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lorem Ipsum

Persistência no banco de dados.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lorem Ipsum

Desenvolvimento da API em Django
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Primeiramente foi criado um novo projeto [#f1]_ no framework Django, através de um template gerado e organizado [#f2]_.


Utilizando o django-rest-framework [#f2]_.

.. todo::

    Mostrar o link do github para o projeto
    Colar aqui a imagem gerado pelo django-rest-framework
    Mostrar como instalar o django-rest-framework
    Mostrar como setar o modulo ao projeto
    Mostrar as configurações basicas para o modulo
    Mostrar a configuracao de permissao na documentação

No Django pode-se organizar em pastas, chamadas de apps, que pode ser criado com o comando *python manage.py startapp api* contendo os arquivos abaixo:

* __init__.py
* models.py
* views.py
* urls.py

O arquivo models contém classes para acessar os contatos conforme o código abaixo.

.. todo::

    Colar aqui o código da classe model Contato
    Mostrar como o django cria varias tabelas alem das principais

.. warning::

    Mostrar o admin do django como funcionalidade top do framework, msm nao sendo o objetivo?

Na views temos a logica para acessar os dados do banco de dados

.. todo::
    Mostrar como instalar a app django-rest-framework
    Colar aqui o código da view Contato

As urls é onde podemos criar as rotas que serão acessadas pelo usuário

.. todo::

    Colar aqui o código da classe model Contato


Como acessar a api criada?

Utilizar o curl
utilizar extensao do chrome POSTMAN
Utilizar o proprio browser

.. [#f1] link do github
.. [#f2] http://www.django-rest-framework.org/
