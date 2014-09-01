Experimentos e resultados
=========================

É um dos capítulos mais importantes, colocando-nos no papel do leitor. São os resultados e as conclusões que interessam de fato ao leitor científico. Aqui, deve-se ter o cuidado de deixar o leitor por dentro de todo o processo do experimento que foi adotado.

TODOS os gráficos, tabelas, números resultantes de sua experimentação devem aparecer aqui, e suas observações (análise crítica) como pesquisador do comportamento destes também.


Ambiente de testes
^^^^^^^^^^^^^^^^^^

Para efetuar os testes, os protótipos tiveram de ser 
colocados em uma ambiente de testes.
Para os dois protótipos, hospedamos a aplicação em uma VPS [#f1]_ da empresa DigitalOcean.

.. [#f1] https://www.digitalocean.com/

O ambiente é composto pelos seguintes componentes de hardware.

+----------------------+--------------------------+
|Componente            |Descrição                 |
+======================+==========================+
|Memória Ram           |512 MegaBytes             |
+----------------------+--------------------------+
|Processador           |1 Core                    | 
+----------------------+--------------------------+
|Espaço em disco       |20 GigaBytes cartão SSD   |
+----------------------+--------------------------+
|Transferência em rede |1 TeraByte                |
+----------------------+--------------------------+


Para os dois protótipos busca-se manter o máximo de igualdade entre os serviços executados, porém, por ser tecnologias diferentes
o modo de *deploy* também são diferentes adicionando ou não novos serviços. As informações dos serviços executados
está listada de acordo com o software de monitoramento [#f2]_ da empresa New Relic.

.. [#f2] https://www.newrelic.com/

No primeiro ambiente com o Node.Js temos os seguintes serviços em execução.

+-----------+---------------+------+-------+-------+
|User       |Process        |Count |CPU    |Memory |
+===========+===============+======+=======+=======+
|pywatch    |gunicorn       |4     | 0.0%  |143 MB |
+-----------+---------------+------+-------+-------+
|lucassimon |node           |1     | 0.0%  |86.2 MB|
+-----------+---------------+------+-------+-------+
|postgres   |postgres       |5     | 0.1%  |18.7 MB|
+-----------+---------------+------+-------+-------+
|root       |supervisord    |1     | 0.0%  |10.6 MB|
+-----------+---------------+------+-------+-------+
|www-data   |nginx          |4     | 0.0%  |8.34 MB|
+-----------+---------------+------+-------+-------+
|root       |rsyslogd       |1     | 0.0%  |5.34 MB|
+-----------+---------------+------+-------+-------+
|newrelic   |nrsysmond      |2     | 0.1%  |3.57 MB|
+-----------+---------------+------+-------+-------+
|root       |getty          |6     | 0.0%  |3.42 MB|
+-----------+---------------+------+-------+-------+
|root       |nginx          |1     | 0.0%  |2.18 MB|
+-----------+---------------+------+-------+-------+
|root       |console-kit-dae|1     | 0.0%  |1.55 MB|
+-----------+---------------+------+-------+-------+
|sshd       |sshd           |1     | 0.0%  |1.5 MB |
+-----------+---------------+------+-------+-------+
|ntp        |ntpd           |1     | 0.0%  |1.41 MB|
+-----------+---------------+------+-------+-------+
|root       |sshd           |1     | 0.0%  |1.31 MB|
+-----------+---------------+------+-------+-------+
|root       |udevd          |1     | 0.0%  |1.09 MB|
+-----------+---------------+------+-------+-------+
|root       |polkitd        |1     | 0.0%  |1,000KB|
+-----------+---------------+------+-------+-------+
|nobody     |memcached      |1     | 0.0%  |816 KB |
+-----------+---------------+------+-------+-------+
|Debian-exim|exim4          |1     | 0.0%  |808 KB |
+-----------+---------------+------+-------+-------+
|root       |cron           |1     | 0.0%  |696 KB |
+-----------+---------------+------+-------+-------+
|messagebus |dbus-daemon    |1     | 0.0%  |696 KB |
+-----------+---------------+------+-------+-------+
|root       |init           |1     | 0.0%  |640 KB |
+-----------+---------------+------+-------+-------+

No segundo protótipo temos os seguintes serviços em execução.

+-----------+---------------+------+-------+-------+
|User       |Process        |Count |CPU    |Memory |
+===========+===============+======+=======+=======+
|pywatch    |gunicorn       |4     | 0.0%  |143 MB |
+-----------+---------------+------+-------+-------+
|lucassimon |node           |1     | 0.0%  |86.2 MB|
+-----------+---------------+------+-------+-------+
|postgres   |postgres       |5     | 0.1%  |18.7 MB|
+-----------+---------------+------+-------+-------+
|root       |supervisord    |1     | 0.0%  |10.6 MB|
+-----------+---------------+------+-------+-------+
|www-data   |nginx          |4     | 0.0%  |8.34 MB|
+-----------+---------------+------+-------+-------+
|root       |rsyslogd       |1     | 0.0%  |5.34 MB|
+-----------+---------------+------+-------+-------+
|newrelic   |nrsysmond      |2     | 0.1%  |3.57 MB|
+-----------+---------------+------+-------+-------+
|root       |getty          |6     | 0.0%  |3.42 MB|
+-----------+---------------+------+-------+-------+
|root       |nginx          |1     | 0.0%  |2.18 MB|
+-----------+---------------+------+-------+-------+
|root       |console-kit-dae|1     | 0.0%  |1.55 MB|
+-----------+---------------+------+-------+-------+
|sshd       |sshd           |1     | 0.0%  |1.5 MB |
+-----------+---------------+------+-------+-------+
|ntp        |ntpd           |1     | 0.0%  |1.41 MB|
+-----------+---------------+------+-------+-------+
|root       |sshd           |1     | 0.0%  |1.31 MB|
+-----------+---------------+------+-------+-------+
|root       |udevd          |1     | 0.0%  |1.09 MB|
+-----------+---------------+------+-------+-------+
|root       |polkitd        |1     | 0.0%  |1,000KB|
+-----------+---------------+------+-------+-------+
|nobody     |memcached      |1     | 0.0%  |816 KB |
+-----------+---------------+------+-------+-------+
|Debian-exim|exim4          |1     | 0.0%  |808 KB |
+-----------+---------------+------+-------+-------+
|root       |cron           |1     | 0.0%  |696 KB |
+-----------+---------------+------+-------+-------+
|messagebus |dbus-daemon    |1     | 0.0%  |696 KB |
+-----------+---------------+------+-------+-------+
|root       |init           |1     | 0.0%  |640 KB |
+-----------+---------------+------+-------+-------+

Num processo científico, devemos ser capazes de repetir o que o autor fez e obter os mesmo resultados. É o chamado “determinismo científico” (em devidas proporções – por exemplo, em sistemas caóticos pode ser difícil obter os mesmos resultados). 

Por esta característica, devemos então ter neste capítulo:

- configurações do experimento (ex: máquina, quantidade de memória, processador, software etc);

  - dados relativos à base de dados (ex: foram usadas 500 imagens de peixes em diferentes situações de iluminação – quais? – e em diferentes épocas do ano – quais?);

  - dados relativos às simplificações usadas (e justificadas).


Testes
^^^^^^

Falar sobre os experimentos realizados e o que se espera de cada um. Em seguida, mostrar estes experimentos e seus resultados e, se possível, comparar resultados esperados X obtidos.

Este é o maior capítulo do texto: 10 páginas ou mais.

Para fazer a simulação e obter os dados dos testes foi utilizado os serviços web loader.io [#f3]_ e blitz.io [#f4]_, que é uma aplicação web desenvolvida para
fazer testes de sobrecarga e mensurar o desempenho de aplicações REST.

Para que os dados fossem os mais próximos possíveis de um ambiente de produção, foi montado dois planos de testes para cada protótipo.
O primeiro plano de teste (Plano de teste A) simula X usuários fazendo requisições distintas ao servidor a cada Y segundos,
Z vezes consecutivas. Isso para o primeiro prototipo. Ja para segundo prototipo simula X usuários fazendo requisições distintas
ao servidor a cada Y segundos, Z vezes consecutivas.

O segundo plano de teste (Plano de teste B) simula X usuários fazendo requisições distintas ao servidor a cada Y segundos,
Z vezes consecutivas, isso para o primeiro prototipo, ja para segundo prototipo simula X usuários fazendo requisições
distintas ao servidor a cada Y segundos, Z vezes consecutivas.

Cada plano de teste foi executado seis vezes para cada protótipo, sendo o maior valor e 
o menor valor dos dados obtidos é eliminado por questões de estatística. Os resultados obtidos
seguem nas tabelas abaixo.

.. [#f3] https://loader.io/

.. [#f4] https://www.blitz.io/

Resultados obtidos no plano de teste A para o primeiro protótipo

.. todo: 
    
    Fazer os resultados

Gráficos de utilização de hardware para o primeiro protótipo

.. todo: 
    
    Fazer os gráficos de acordo com a new-relic

Resultados obtidos no plano de teste A para o segundo protótipo

.. todo: 
    
    Fazer os resultados

Gráficos de utilização de hardware para o segundo protótipo

.. todo: 
    
    Fazer os gráficos de acordo com a new-relic



Resultados obtidos no plano de teste B para o primeiro protótipo

.. todo: 
    
    Fazer os resultados

Gráficos de utilização de hardware para o primeiro protótipo

.. todo: 
    
    Fazer os gráficos de acordo com a new-relic



Resultados obtidos no plano de teste B para o segundo protótipo

.. todo: 
    
    Fazer os resultados

Gráficos de utilização de hardware para o segundo protótipo

.. todo: 
    
    Fazer os gráficos de acordo com a new-relic




