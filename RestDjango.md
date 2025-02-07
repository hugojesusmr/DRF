# 0.- DJANGO REST FRAMEWORK (DRF)

* Es una herramienta para la creación de APIS REST Web, esta basado en framework de desarrollo web backend django el cual esta escrito en python.
Esta basado netamente en Django, Django Rest Framework es una modificación de Django, es decir, han tomando com tal al Framework DJango robusto y lo han estructurado para crear herramientas, clases etc, para adecuarlo a la arquitectura REST, y se definieron este tipo de herramientas para que sea mas facil trabajar con REST porque con DJANGO normal no existen uno tiene que crearlas.

# 0.1.- ¿CUAL ES MAS COMPLETO?

* DJANGO REST FRAMEWORK (DRF) porque incorpora DJANGO bajo la arquitectura que se define de API REST como tal.

# 1.- INTERFAZ DE PROGRAMACIÓN DE APLICACIONES (API)    

Ejemplo:

Imagina que tenemos una aplicación Móvil, Aplicación Web y Aplicación de Escritorio y lo que se requiere es que
todas las aplicaciones se comuniquen entre si, y cada una de ellas puede estar desarrollada en cualquier lenguaje.

 # 1.1 ¿COMO SE HACE PARA QUE LAS APLICACIONES SE COMUNIQUEN ENTRE ENTRE SI?

* Aqui es donde entran las [API'S], que se encargan de comunicar a todas las aplicaciones, en el ejemplo anterior se tienen los tres tipos de aplicaciones, la API entra a enlazar las 3 aplicaciones mencionadas. Esta comunicación se realiza a travez de [REST], va a definir una serie de características que son comunes para todas.

* Las API'S sirven como una interfaz para intercomunicarse basandose en unos conceptos que define REST.

* Para que todo se mantenga estandar y se comuniquen sin ningun problema, tomando el protocolo http que existe en la WEB, estandarizando la trasnferencia de datos, utilizando los diversos metodos como: [GET, POST, DELETE, PUT], son los métodos que va a utilizar el cliente para comunicarse al servidor tomando la API aplicando ciertas reglas. 

Como: 

* En el Servidor solo Existe la Lógica.
* Tener por separado el cliente o [Frontend] que se considera la interfaz como tal(estilos, html, js, etc)
* Dejar de tener en [Backend] Templates, es decir dejar de renderizar plantillas, css, js, etc. no deben de existir ningun tipo de archivo en servidor.

Combinado el concepto hace [REST + API]

                      [Aplicación_Web]
                             |
                             |
                             |
 [Aplicación_Móvil]------> [API] <----------[Aplicación_Escritorio]                    


# 2.- ¿QUÉ SIGNIFICA [REST]? = [TRANSFERENCIA_DE_ESTAD0_REPRESENTACIONAL] 

# 3.- ¿QUE VA HACER LA REST API?

* Por lo general el valor de retorno se realiza por medio de [JSON] que es el estandar ó [XML] y que son los formatos que van a tener vinculo con la [API] y puedan retornar los datos.

# 4.- MÉTODOS HTTP

* GET                
* POST               
* PUT                 
* DELETE                   

* [REST] define que la petición no debe de tener un estado, es decir, tiene que estar sin estado no tiene que depender o estar a la espera de otra petición para poder procesar y responder.

Ejemplo:

* El cliente hace la petición, el servidor la procesa y responde a esto se refiere cuando la API no tiene que tener estado.
* Hay que indicar con la información que devolvemos al navegador los codigos de estado como los siguientes:


# 5.- CÓDIGOS DE ESTADO

 * Son [4] códigos de estados que define el protocolo [http] [20X], [30X], [40X], [50X] se definen a continuación:


# 5.1 CÓDIGO DE ESTADO 20X [CORRECTO]

* Cuando en el navegador se hace una petición, reconoce un estado, si la respuesta es correcta es un estado [200] que básicamente es un 200.
* Cuando el cliente envie información para que se guarde en la Base de Datos, lo correcto en retornar es un código de estado [201] que significa que ha sido creada la instancia que se ha enviado para que se registre.

# 5.2 CÓDIGO DE ESTADO 30X [CACHÉ_REDIRECCIONAMIENTO]

* Hace referencia a metodos de cache o redireccionamiento, cuando el cliente va a redireccionar alguna url, lo que hace básicmante es enviar un código 300 para que el navegador interprete esto y diga, me va a redirecionar o si se requiere permiso del servidor para redireccinar algo.

* La tarea principal es dar una respuesta para que redireccione es retornar un código [300].

# 5.3 CÓDIGO DE ESTADO 40X [NO_ENCONTRÁDO]

Es donde se manejan los posibles errores com [404] que no se encontro [NOT_FOUND] etc. 

# 5.4 CÓDIGO DE ESTADO 50X[ERROR_DE_SERVIDOR] 

* Error de servidor, esto sucede cuando el cliente hace una petición y en servidor una variable esta mal colocada, no existe la variable a la que se llama, esta mal capturada la forma de enviar los datos, básicamente errores de programación que el servidor no puede reconocer porque le faltan caracteristicas y el navegador retorna un aviso de error 500.

* Lo que define REST y lo que define API juntos hacen [RESTAPI] que es una forma o una arquitectura de como estructurar todo un proyecto pqra poder realizar este tipo de aplicaciones como tal y que pueden comunicarse con diferentes clientes sin importar la tecnologia donde esten desarrollados.


# 6.- DIFERENCIAS ENTRE [DJANGO] Y [DJANGO_REST_FRAMEWORK]

  * La forma de realizar las peticiones en el framework django por decir normal se hace mediante [request], que es el parámetro que envia a toda  función o toda vista basada en clase.

  * En [DJANGO_REST_FRAMEWORK] No existe [request.POST] ha sido remplazado

  Ejemplo:
         [DJANGO_FRAMEWORK]            [DJANGO_REST_FRAMEWORK]
                |                           |
                |                           |
                |                           |
       * [request.POST] ----> [request.data(incluye archivos o parametros enviados)]
       * [request.GET]  ----> [request.query_params]


  # 7.- VARIABLES DENTRO DE REQUEST

  * Dentro de request cuando uno realiza una petición el [Frontend] realiza una petición a mi [Backend], en lo que el servidor recoge la petición hay algo que se llama negociación y a que se refiere con esto, a que el Backend va a interpretar lo que el [Frontend] le ha enviado y va a devolver una respuesta.

  * Por defecto [request] va a delvolver un parámetro que se llama [accepted_render] que es el que decide que tipo de formato se va retornar. 

  * [accepted_render] Es una instancia de una clase que define un render y un render basicamente es como se va a pintar la información en el navegador, en este caso DRF esta basado en rest y define que tienes que devolver JSON o XML, por lo tanto [accepted_render] cada vez que reconoce una petición se setea y se coloca como una instancia de JSONRender es decir se va a retornar un JSON

     [REQUEST]                  [DATA]

    accepted_render      -------> JSONRenderer()
    accepted_media_type  -------> application/json  (contenido medio, imagenes, archivos, etc)

Solo se retorna JSON

 # 8.- COMO SE SOLUCIONA ESTO

 Django Rest Framework definio esto: 

[RESPONSE]: Que es una clase que Hereda de Simple Template Response y lo que define básicamente que se va a retornar. 
Lo que tiene en su estructura y que es la clase por defecto va a retornar de información basicamente es enviame , la consulta, los datos, y request se encarga de recoger esa data seteada y como se va a retornar.


            |          
            |   
 Response(data, status=None, template_name = None, headers=None, content_type=None)

 * data = Son los datos ya serializados que se envian como respuesta
 * status = codigo HTTP de estado para la respuesta, por defecto retorna codigo HTTP_200_OK
 * template_name = plantilla a utilizar si es que se utiliza htmlrender 
 * content_type = tipo de contenido de la respuesta, es definido automaticamante      

