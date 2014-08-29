O ambiente Node.Js
==================


Programação Orientada a eventos
-------------------------------

PEREIRA (2012) compara que o Node.Js orientado a eventos se espelha na filosofia de orientação a eventos
utilizado pelo JavaScript nos navegadores; a diferença entre eles é que no  Node.Js não existe eventos
de clique do mouse, teclas pressionadas do teclado -keyup- ou qualquer evento de componentes HTML.
No Node.Js os eventos trabalhados são entrada e saída do servidor como eventos de conexão ao banco de dados,
abertura de arquivo e um dado de um *streaming*, dentre muitos outros.

Single – Thread
---------------

Uma das melhores maneiras para entender o *single-thread*  é descrita por Tom Hughes e Mike Wilson (2012)
fazendo uma analogia a nossa vida, segue síntese do texto abaixo:

Na vida cotidiana, estamos acostumados todos os tipos de retorno de chamadas internas para lidar com eventos, e ainda,
como JavaScript fazemos apenas uma coisa de cada vez. De maneira divertida HUGHES e WILSON exemplifica
que você é capaz de esfregar a barriga e coçar a cabeça, ao mesmo tempo, certo!?
Mas se você realizar uma atividade mais grave, ao mesmo tempo, algo irá dar errado muito rapidamente.
Isto é como JavaScript.
É ótimo as ações serem conduzidas por eventos mas no *single-thread* apenas uma coisa acontece ao mesmo tempo.

Para Tom Hughes e Mike Wilson (2012) o conceito *single-threaded* é muito importante porém é uma das críticas feitas ao Node.Js
é a falta de concorrência.
Quando Tom Hughes e Mike Wilson (2012) pronunciou falta de concorrência quis dizer que não é utilizado todas as CPU's
de um computador. Segundo estes autores o problema de executar códigos em várias CPU's de uma vez é que ele requer
uma coordenação entre várias “linhas” de execução.
Para que várias CPU's possam dividir de maneira eficaz o trabalho, é necessário que eles conversem entre si
sobre o estado atual do programa, e o que cada single *thread* havia feito.

Tom Hughes e Wilson não descarta a possibilidade de concorrência mas que é um modelo mais complexo e que exige
mais esforço do desenvolvedor e do sistema. 

De acordo com PEREIRA (2012), em Node.Js nativamente não é possível trabalhar com programação concorrente em plataforma *multi-thread*.
Mas que existem maneiras de se implementar sistemas concorrentes, como por exemplo, utilizar *clusters* o qual é um módulo nativo
do ambiente Node.Js.

Powers (2012) cita também o single *thread* como um dos benefícios do ambiente do Node.Js pois o aplicativo pode ser
facilmente escalável uma vez que em um único segmento de execução não ha uma enorme sobrecarga de requisições.
Citando o exemplo de seu livro, ao criar uma aplicação em PHP semelhante à aplicação Node.Js o usuário veria a mesma página,
mas no código *backend* do sistema ira notar-se a diferença.

Se executar esse aplicativo PHP no servidor web Apache , cada pedido que for solicitado irá ser tratado em um processo filho separado.
As possibilidades são, a menos que você tem um sistema de carregamento eficiente,
você só vai ser capaz de executar mais um par de centenas de processos filhos em paralelo.
Mais do que esse número de pedidos significa que um cliente precisa esperar por uma resposta. (POWERS, 2012)

Chamadas de retorno e chamadas de retorno infernais
---------------------------------------------------

De acordo com WILSON (2013) o JavaScript utiliza de *callbacks* para abordar o problema a partir do lado oposto;
ao invés de gerenciar processos de execução prolongada, os desenvolvedores associam eventos específicos e
escrevem funções especiais, chamadas *callbacks*, que são executadas quando o critério do evento é atingido.

Evitando chamadas de retorno infernais
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PEREIRA (2012) relata que é o JavaScript é perfomático trabalhando de forma assíncrona  porém em certos
momentos do desenvolvimentos, inevitavelmente será implementado diversas funções assíncronas encadeadas
umas nas outras através das suas funções *callbacks*.

.. code-block:: javascript
    :linenos:

    var fs = require('fs');
    fs.readdir(__dirname, function(erro, contents) {
        if (erro) { throw erro; }
        contents.forEach(function(content) {
            var path = './' + content;
            fs.stat(path, function(erro, stat) {
                if (erro) { throw erro; }
                if (stat.isFile()) {
                    console.log('%s %d bytes', content, stat.size);
                }
            });
        });
    });

Com o código exemplificado por PEREIRA (2012) temos uma simples leitura dos arquivos do diretório e imprimindo
o nome e o tamanho em bytes.
Com este exemplo PEREIRA (2012) nos demonstra que uma simples tarefa possui muitos encadeamentos e nos questiona
como seria a organização caso seja uma função complexa.
Praticamente o código implementado seria um caos e de difícil manutenabilidade. 

Pela linguagem JavaScript ser assíncrona PEREIRA (2012) afirma que neste amaranhado de *callbacks* 
podemos perder o controle do que está sendo executado, perder acesso a variáveis devido a troca de escopos
em troca de ganhos com a performance.

Nos *callbacks* do Node.Js é importante atentar como feito por PEREIRA (2012) que em sua maioria possuem
como parâmetro uma variável de erro.
Caso exista esse parâmetro é recomendado por PEREIRA (2012) realizar o tratamento deles na execução do *callback*
impedindo a execução aleatória quando for identificado um erro.

Existem várias maneiras de se evitar o temido *callback hell*, como sugerido por PEREIRA (2012), uma boa prática
de código JavaScript é criar funções que expressem seu objetivo e de forma isoladas, 
salvando em variável e passando-as em *callback*.
Veja o exemplo abaixo do arquivo *callback_heaven.js* criado por PEREIRA (2012).

.. code-block:: javascript
    :linenos:

    var fs = require('fs');
    var lerDiretorio = function() {
        fs.readdir(__dirname, function(erro, diretorio) {
            if (erro) return erro;
            diretorio.forEach(function(arquivo) {
                ler(arquivo);
            });
        });
    };

    var ler = function(arquivo) {
        var path = './' + arquivo;
        fs.stat(path, function(erro, stat) {
            if (erro) return erro;
            if (stat.isFile()) {
                console.log('%s %d bytes', arquivo, stat.size);
            }
        });
    };

    lerDiretorio();


Como dito por PEREIRA (2012) houve uma melhora na legibilidade do código, deixando mais semântico e legível
o nome das funções. O número de *callbacks* encadeados também diminui.
PEREIRA (2012) sugere como boa prática manter no máximo dois encadeamentos de *callback*, caso passe esse número
é interessante criar uma função externa para ser passada como parâmetro nos *callbacks*, ao invés de continuar criando *callbacks hell*.

.. warning::

    Novas técnicas de callback hell:

    `Artigo 1`_
    `Artigo 2`_


.. _Artigo 1: http://lostechies.com/bradcarleton/2014/02/18/taming-callback-hell-in-node-js/
.. _Artigo 2: http://strongloop.com/strongblog/node-js-callback-hell-promises-generators/


Ciclo de eventos
----------------

Ao introduzir esse assunto PEREIRA (2012) diz que o ciclo de eventos - *Event-Loop* - é o agente responsável
por escutar e emitir eventos dentro do sistema.
PEREIRA (2012) rapidamente explica essa teoria do paradigma orientação a eventos o ciclo de eventos é uma repetição infinita
que a cada interação verifica em sua fila de eventos se um determinado evento foi emitido ou se existem novos eventos.
Estes eventos só aparecem na fila quando são emitidos durante as suas interações na aplicação; quando ocorre,  é emitido um evento,
então este evento é executado e enviados para a fila de executados. 

WILSON (2013) enaltece os eventos como sendo a alma do Node.Js e do JavaScript.
Complementando WILSON (2013) afirma que outras linguagens de programação lidam com fluxos de trabalho em *threads*
múltiplas e concorrentes, com cada *thread*  gastando a maioria de seu tempo aguardando operações
bloqueadoras de entrada e saída como leitura ou escrita em disco, manipulação do banco de dados ou acesso a informações pela rede.

Veja a figura abaixo [Ref]_ 

.. image:: ../_static/event-loop-caio-ribeiro.png
    :alt: Ciclo de eventos no Node.Js
    :align: center

.. [Ref] Retirado do livro Aplicações web real-time com Node.Js 

WILSON (2013) escreve uma das qualidades do JavaScript, que foi criado seguindo o modelo de programação orientado a eventos.
Sendo desde um simples clique de mouse, carregamento de páginas ou envio de formulários, todos utilizando o modelo baseado em eventos.

O *event-loop* – cilo de eventos – é o sistema que usa o JavaScript para lidar com os pedidos recebidos
de várias partes do sistema de uma forma sadia. Há uma série de maneiras como as pessoas lidam com o “tempo real” ou questões “paralelas” em computação.
A maioria deles são bastante complexos e fazem o cérebro doer.
O JavaScript tem uma abordagem simples que torna o processo muito mais compreensível,
mas introduz algumas restrições.
Possuindo uma ideia de como o ciclo de eventos funciona, o desenvolvedor é capaz de usá-lo em toda sua potencialidade,
conseguindo vantagens e evitando armadilhas dessa abordagem.( Tom Hughes-Croucher e Mike Wilson, 2012)

.. warning ::
  
    Corrigir o ( Tom Hughes-Croucher e Mike Wilson, 2012)

Pensamos que a maioria das pessoas entendem intuitivamente a programação orientada a eventos, porquê é como a vida cotidiana. 
Imagine que você esta cozinhando. Você esta cortando um pimentão e uma panela começa a ferver. Você termina de cortar e, em seguida desliga o fogão.
Ao invés de tentar cortar e desligar o fogão, ao mesmo tempo, você irá alcançar o mesmo resultado de uma forma mais segura 
através dessa rápida mudança de contextos.

A programação orientada a eventos faz a mesma coisa. Ao permitir que o desenvolvedor escreva código que só trabalhe em um retorno
de chamada de cada vez, o programa será compreensível e também capaz de executar rapidamente várias tarefas de forma eficiente.( Tom Hughes-Croucher e Mike Wilson, 2012)

.. warning ::
  
    Corrigir o ( Tom Hughes-Croucher e Mike Wilson, 2012)

Continuando, como apresentado por PEREIRA (2012) o *EventEmitter*, é o módulo responsável por por emitir estes eventos e em
grande maioria das bibliotecas do ambiente Node.Js utiliza as funcionalidades de eventos deste módulo.
No processo de execução do evento pode-se programar qualquer lógica de programação através do mecanismo de
*callback* - chamada de retorno - , tal *callback* - chamada de retorno -pode ser executado através de uma função de escuta, semanticamente conhecida pelo *on()*.

Essa seção é bem descrita e exemplificada por WILSON (2013) em seu livro que nos mostra o uso e o desenvolvimento de eventos.

.. code-block:: javascript
    :linenos:

    var events = require('events')
    var eventEmitter = new events.EventEmitter();

    function mainLoop() {
        console.log('Starting application');
        eventEmitter.emit('AplicationStart');

        console.log('Running application');
        eventEmitter.emit('AplicationRun');
        
        console.log('Stopping application');
        eventEmitter.emit('AplicationStop');
    }

    function onApplicationStart() {
        console.log('Handling Application Start Event');
    }

    function onApplicationRun() {
        console.log('Handling Application Run Event');
    }

    function onApplicationStop() {
        console.log('Handling Application Stop Event');
    }

    eventEmitter.on('ApplicationStart', onApplicationStart);
    eventEmitter.on('ApplicationRun', onApplicationRun);
    eventEmitter.on('ApplicationStop', onApplicationStop);

    mainLoop();


Segundo Wilson (2013) o exemplo acima demonstra como três funções não relacionadas **onApplicationStart**, 
**onApplicationRun** e **onApplicationStop** podem ser encadeadas para produzir a saída ::

    Starting application
    Handling Application Start Event

    Running application
    Handling Application Run Event

    Stopping application
    Handling Application Stop Event


Os eventos **ApplicationStart, ApplicationRun e ApplicationStop** são registrados utilizando o *eventEmitter* no método
antes de a função **mainLoop** ser executada. Isso inclui um ouvinte de evento para cada um desses eventos - de agora em diante,
sempre que qualquer evento for levantado, ele será verificado de acordo com esses ouvintes para determinar se uma correspondência
está disponível, caso em que a função de *callback* - chamada de retorno - dessa correspondência será executada. (WILSON, 2013)

A saída de tela destaca um traço importante do Node.Js: todo o seu trabalho é feito em uma única *thread*. Quando um evento é levantado
e respondido por um *callback* - chamada de retorno -, o método de chamada é pausado enquanto o *callback* é executado. Isso é importante 
porque, se algo acontecer durante o *callback* e consumir bastante tempo de processamento, a função original não vai continuar
sendo executada até que todo o trabalho esteja completado.

.. warning ::

    Não entendi essa última parte o Node.Js não é bloqueante. Mas em eventos eles espera o processamento terminar?

Assim, a execução desse exemplo segue o caminho: ::

    1. Executa **mainloop**, dispara **ApplicationStartEvent**.
    2. Executa o *callback* **onApplicationStart**.
    3 Continua a execução de **mainloop**, dispara **ApplicationRun**.
    4. Executa o *callback* **onApplicationRun**.
    5. Continua a execução de **mainloop**, dispara **ApplicationStop**.
    6. Executa o *callback* **onApplicationStop**.
    7. Retorna para a execução de **mainLoop**, não há mais nada a fazer; para.


Finalizando esta seção, PEREIRA (2012) diz que o *event-driven* do Node.Js foi inspirado pelos frameworks
Event Machine do Ruby e Twisted do Python, porém o ciclo de eventos do Node.Js é mais perfomático pois seu mecanismo
é nativamente executado de forma não bloqueante sendo o diferencial em relação a outros ambientes de programação.


Por que usar assíncrono
-----------------------

No ambiente de desenvolvimento Node.Js é importante entender e saber trabalhar com as chamadas assíncronas.
PEREIRA (2012) exemplifica em código as diferenças entre uma função síncrona e assíncrona em relação ao tempo
em que são executadas.
O código é para criar uma repetição de 5 interações e a cada iteração desta repetição será criado um arquivo texto.

.. code-block:: javascript
    :linenos:

    var fs = require('fs');
    
    for(var i = 1; i <= 5; i++) {
        var file = "sync-txt" + i + ".txt";
        var out = fs.writeFileSync(file, "Hello Node.js!");
        console.log(out);
    }

Veja o tempo gasto no modelo síncrono [Ref]_:

.. image:: ../_static/timeline-node-sync-caio-ribeiro.png
    :alt: Tempo de execução síncrono no Node.Js
    :align: center

.. [Ref] Retirado do livro Aplicações web real-time com Node.Js 

.. code-block:: javascript
    :linenos:

    var fs = require('fs');
    
    for(var i = 1; i <= 5; i++) {
        var file = "async-txt" + i + ".txt";
        fs.writeFile(file, "Hello Node.js!", function(err, out) {
            console.log(out);
        });
    }


.. image:: ../_static/timeline-node-async-caio-ribeiro.png
    :alt: Tempo de execução assíncrono no Node.Js
    :align: center

Threads versus Assincronismos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

De acordo com PEREIRA (2012) por mais que as funções assíncronas possam executar em paralelo várias tarefas,
elas jamais serão consideradas uma *Thread* ( como *Threads* do java).
A diferença é que as *Threads* são manipuláveis pelo desenvolvedor, ou seja, você pode pausar a execução de uma *Thread*
ou fazê-la esperar o término de uma outra.
Chamadas assíncronas apenas invocam suas funções numa ordem de que você não tem controle,
e você só sabe quando uma chamada terminou quando seu *callback* é executado. 

Pode parecer vantajoso ter controle sobre *Threads* a favor de um sistema que executa tarefas em paralelo,
mas pouco domínio sobre eles pode transformar seus sistema em um caos de travamentos *deadlocks*, 
afinal *threads* são executadas de forma bloqueante. Este é o grande diferencial das chamadas assíncronas,
elas executam em paralelo suas funções sem travar processamento das outras e principalmente sem bloquear o sistema principal.

.. warning:: 

    Aqui deveria mostrar um exemplo de código em python e outro em node?

    `Code Python 1`_
    `Code Python 2`_
    `Code Python 3`_
    `Code Python 4`_
    `Code Python 5`_


.. _Code Python 1: http://www.vivaolinux.com.br/artigo/Threads-Importancia-dentro-de-um-software?pagina=1

.. _Code Python 2: http://medeubranco.wordpress.com/2008/07/10/threads-em-python/

.. _Code Python 3: http://imasters.com.br/artigo/20127/py/threads-em-python/

.. _Code Python 4: http://pythonrs.wordpress.com/2010/03/12/python-com-threads/

.. _Code Python 5: http://darkstrikerd.wordpress.com/2012/04/12/threads-simples-com-python/

    

Como dito por PEREIRA (2012) é essencial que seu código Node.Js invoque o mínimo possível de funções bloqueantes.
Toda função síncrona impedirá, naquele instante, que o Node.Js continue executando os demais códigos até que aquela
função seja finalizada.
Por exemplo, se essa função fizer uma operação de entrada e saída em disco, vai bloquear o sistema inteiro,
deixando o processador ocioso enquanto é utilizado outros recursos de hardware.

