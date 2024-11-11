from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Juego de Preguntas")
#root.iconbitmap("icono.ico")
root.geometry("900x600")
root.config(bg="black")
root.resizable(0, 0)

#background_image = Image.open("galaxia.jpg")
#background_photo = ImageTk.PhotoImage(background_image)

#background_label = Label(root, image=background_photo)
#background_label.place(relwidth=1, relheight=1)

questions = [
    {
        "question": "¿Qué protocolo de internet se utiliza para enviar correos electrónicos?",
        "options": ["a) FTP", "b) HTTP", "c) SMTP", "d) SSH"],
        "correct": 2,
    },
    {
        "question": "¿Cuál de las siguientes opciones NO es un lenguaje de programación?",
        "options": ["a) Java", "b) HTML", "c) CSS", "d) Photoshop"],
        "correct": 3,
    },
    {
        "question": "¿Qué tipo de memoria es más rápido pero también más costoso?",
        "options": ["a) RAM", "b) Disco duro", "c) SSD", "d) Pendrive"],
        "correct": 0,
    },
    {
        "question": "¿Cuál de las siguientes opciones es un sistema operativo de código abierto?",
        "options": ["a) Windows", "b) macOS", "c) Linux", "d) iOS"],
        "correct": 2,
    },
    {
        "question": "¿Cuál de las siguientes opciones es una base de datos relacional?",
        "options": ["a) MongoDB", "b) PostgreSQL", "c) Redis", "d) Cassandra"],
        "correct": 1,
    },
    {
        "question": "¿Qué significa la sigla 'PDF' en informática?",
        "options": [
            "a) Page Description Format",
            "b) Personal Document Format",
            "c) Portable Data File",
            "d) Print Document File",
        ],
        "correct": 1,
    },
    {
        "question": "¿Qué protocolo se utiliza para acceder a sitios web seguros?",
        "options": ["a) HTTP", "b) FTP", "c) HTTPS", "d) SMTP"],
        "correct": 2,
    },
    {
        "question": "¿Cuál de las siguientes opciones es un lenguaje de marcado utilizado para estructurar contenido en la web?",
        "options": ["a) Java", "b) Python", "c) XML", "d) Ruby"],
        "correct": 2,
    },
    {
        "question": "¿Qué dispositivo de entrada se utiliza comúnmente para mover el cursor en una pantalla?",
        "options": ["a) Teclado", "b) Ratón", "c) Micrófono", "d) Altavoz"],
        "correct": 1,
    },
    {
        "question": "¿Qué componente de hardware se encarga de realizar cálculos y procesar datos en una computadora?",
        "options": [
            "a) Disco duro",
            "b) CPU (Unidad Central de Procesamiento)",
            "c) RAM",
            "d) Tarjeta gráfica",
        ],
        "correct": 1,
    },
    {
        "question": "¿Qué tipo de ataque informático busca engañar a las personas para obtener información confidencial?",
        "options": ["a) Ataque DDoS", "b) Malware", "c) Phishing", "d) Exploit"],
        "correct": 2,
    },
    {
        "question": "¿Cuál de las siguientes opciones NO es un navegador web?",
        "options": [
            "a) Google Chrome",
            "b) Microsoft Word",
            "c) Mozilla Firefox",
            "d) Safari",
        ],
        "correct": 1,
    },
    {
        "question": "¿Cuál de las siguientes opciones es una red inalámbrica de corto alcance?",
        "options": ["a) WAN", "b) LAN", "c) Bluetooth", "d) Ethernet"],
        "correct": 2,
    },
    {
        "question": "¿Qué sistema operativo es desarrollado por Apple Inc.?",
        "options": ["a) Windows", "b) Ubuntu", "c) macOS", "d) Fedora"],
        "correct": 2,
    },
    {
        "question": "¿Qué tecnología permite que los dispositivos se comuniquen entre sí tocándose o acercándose?",
        "options": [
            "a) NFC (Near Field Communication)",
            "b) GPS",
            "c) Bluetooth",
            "d) Wi-Fi",
        ],
        "correct": 0,
    },
    {
        "question": "¿Qué es un firewall en el contexto de la seguridad informática?",
        "options": [
            "a) Un dispositivo de almacenamiento",
            "b) Un programa de edición de imágenes",
            "c) Un componente de hardware que protege una red",
            "d) Un lenguaje de programación",
        ],
        "correct": 2,
    },
    {
        "question": "¿Cuál de las siguientes opciones es un servicio de almacenamiento en la nube?",
        "options": [
            "a) Microsoft Office",
            "b) Dropbox",
            "c) Adobe Photoshop",
            "d) Notepad",
        ],
        "correct": 1,
    },
    {
        "question": "¿Qué lenguaje de programación es ampliamente utilizado para el desarrollo de aplicaciones móviles?",
        "options": ["a) Java", "b) C++", "c) Ruby", "d) PHP"],
        "correct": 0,
    },
    {
        "question": "¿Cuál de las siguientes opciones se utiliza para dar estilo y diseño a páginas web?",
        "options": ["a) HTML", "b) Python", "c) CSS", "d) JavaScript"],
        "correct": 2,
    },
    {
        "question": "¿Cuál de las siguientes opciones es un ejemplo de un sistema operativo de código abierto?",
        "options": ["a) Windows", "b) macOS", "c) Linux", "d) Android"],
        "correct": 2,
    },
    {
        "question": "¿Qué es una base de datos?",
        "options": [
            "a) Un conjunto de hojas de cálculo",
            "b) Un conjunto de archivos de texto",
            "c) Una colección organizada de datos relacionados",
            "d) Un conjunto de imágenes",
        ],
        "correct": 2,
    },
    {
        "question": "¿Cuál de las siguientes declaraciones describe mejor a un sistema de gestión de bases de datos (DBMS)?",
        "options": [
            "a) Una herramienta para diseñar gráficos",
            "b) Un software para administrar y organizar bases de datos",
            "c) Una aplicación de edición de texto",
            "d) Un servicio de correo electrónico",
        ],
        "correct": 1,
    },
    {
        "question": "¿Qué es SQL?",
        "options": [
            "a) Un lenguaje de programación visual",
            "b) Un lenguaje de marcado para la web",
            "c) Un lenguaje de consulta estructurado para bases de datos",
            "d) Un lenguaje de programación orientado a objetos",
        ],
        "correct": 2,
    },
    {
        "question": "¿Qué tipo de clave se utiliza para establecer relaciones entre tablas en una base de datos relacional?",
        "options": [
            "a) Clave principal",
            "b) Clave extranjera",
            "c) Clave única",
            "d) Clave candidata",
        ],
        "correct": 3,
    },
    {
        "question": "¿Cuál de las siguientes opciones describe mejor una base de datos relacional?",
        "options": [
            "a) Almacena datos en una sola tabla",
            "b) Almacena datos en múltiples tablas relacionadas",
            "c) Almacena solo números enteros",
            "d) Almacena solo imágenes",
        ],
        "correct": 1,
    },
    {
        "question": "¿Cuál de las siguientes operaciones en SQL se utiliza para recuperar datos de una base de datos?",
        "options": ["a) INSERT", "b) DELETE", "c) UPDATE", "d) SELECT"],
        "correct": 3,
    },
    {
        "question": "¿Qué tipo de base de datos está optimizado para el procesamiento y análisis de grandes volúmenes de datos?",
        "options": [
            "a) Base de datos relacional",
            "b) Base de datos en memoria",
            "c) Base de datos distribuida",
            "d) Base de datos de análisis",
        ],
        "correct": 0,
    },
    {
        "question": "¿Qué es la normalización en el contexto de las bases de datos?",
        "options": [
            "a) Un proceso para denormalizar datos",
            "b) Un proceso para dividir datos en múltiples tablas",
            "c) Un proceso para mejorar la eficiencia del servidor",
            "d) Un proceso para reducir la seguridad de la base de datos",
        ],
        "correct": 1,
    },
    {
        "question": "¿Qué tipo de base de datos es más adecuado para aplicaciones que requieren alta velocidad y baja latencia?",
        "options": [
            "a) Base de datos relacional",
            "b) Base de datos en memoria",
            "c) Base de datos documental",
            "d) Base de datos de columnas",
        ],
        "correct": 1,
    },
    {
        "question": "¿Qué es la integridad referencial en una base de datos?",
        "options": [
            "a) La capacidad de mantener múltiples copias de la base de datos",
            "b) La capacidad de ocultar datos sensibles",
            "c) La garantía de que las relaciones entre tablas sean consistentes y válidas",
            "d) La garantía de que los datos se almacenan en orden alfabético",
        ],
        "correct": 2,
    },
    {
        "question": "¿Cuál de las siguientes bases de datos es una base de datos NoSQL?",
        "options": ["a) MySQL", "b) PostgreSQL", "c) MongoDB", "d) Oracle"],
        "correct": 2,
    },
    {
        "question": "¿Qué tipo de base de datos es eficiente para almacenar y consultar datos jerárquicos, como documentos JSON?",
        "options": [
            "a) Base de datos relacional",
            "b) Base de datos en memoria",
            "c) Base de datos documental",
            "d) Base de datos de columnas",
        ],
        "correct": 2,
    },
    {
        "question": "¿Qué es un 'join' en SQL?",
        "options": [
            "a) Un tipo de consulta que combina datos de múltiples tablas",
            "b) Un comando para eliminar registros de una tabla",
            "c) Un comando para actualizar registros en una tabla",
            "d) Un comando para agregar nuevos registros a una tabla",
        ],
        "correct": 0,
    },
    {
        "question": "¿Cuál de las siguientes opciones es una característica de las bases de datos NoSQL?",
        "options": [
            "a) Estructura rígida y predefinida",
            "b) Uso exclusivo de SQL para consultas",
            "c) Escalabilidad horizontal sencilla",
            "d) Adherencia estricta a la normalización",
        ],
        "correct": 2,
    },
    {
        "question": "¿Qué es un índice en una base de datos?",
        "options": [
            "a) Un campo de texto largo",
            "b) Un campo que almacena imágenes",
            "c) Una estructura que mejora la velocidad de búsqueda",
            "d) Un tipo especial de clave primaria",
        ],
        "correct": 2,
    },
    {
        "question": "¿Qué es la acididad en una base de datos?",
        "options": [
            "a) Un concepto relacionado con la seguridad de la base de datos",
            "b) Un modelo de datos jerárquico",
            "c) Un conjunto de propiedades que garantizan la consistencia y la integridad de los datos",
            "d) Una medida de la velocidad de la base de datos",
        ],
        "correct": 2,
    },
    {
        "question": "¿Qué tipo de base de datos se utiliza comúnmente para almacenar información en forma de pares clave-valor?",
        "options": [
            "a) Base de datos relacional",
            "b) Base de datos en memoria",
            "c) Base de datos de documentos",
            "d) Base de datos de grafos",
        ],
        "correct": 1,
    },
    {
        "question": "¿Qué es la partición en una base de datos distribuida?",
        "options": [
            "a) Un proceso para dividir una tabla en múltiples tablas más pequeñas",
            "b) Un proceso para copiar datos de una base de datos a otra",
            "c) Un proceso para encriptar los datos en la base de datos",
            "d) Un proceso para crear copias de seguridad",
        ],
        "correct": 0,
    },
    {
        "question": "¿Cuál de las siguientes bases de datos está diseñada específicamente para el análisis de datos en línea?",
        "options": [
            "a) OLTP (Procesamiento de transacciones en línea)",
            "b) OLAP (Procesamiento analítico en línea)",
            "c) NoSQL",
            "d) MongoDB",
        ],
        "correct": 1,
    },
    {
        "question": "¿Qué es la consistencia eventual en una base de datos distribuida?",
        "options": [
            "a) Garantiza que todos los nodos de la base de datos tengan la misma información en todo momento",
            "b) Garantiza que los datos se replican en todos los nodos de inmediato",
            "c) Permite que los nodos de la base de datos tengan diferentes versiones de los datos temporalmente",
            "d) Garantiza que los datos se almacenan en una sola ubicación para facilitar la administración",
        ],
        "correct": 0,
    },
    {
        "question": "¿Qué tipo de lenguaje de programación es Python?",
        "options": [
            "a) Lenguaje de programación compilado",
            "b) Lenguaje de programación interpretado",
            "c) Lenguaje de programación ensamblador",
            "d) Lenguaje de programación de bajo nivel",
        ],
        "correct": 1,
    },
    {
        "question": "¿Qué símbolo se utiliza para comentarios de una sola línea en Python?",
        "options": ["a) //", "b) --", "c) ##", "d) /* */"],
        "correct": 2,
    },
    {
        "question": "¿Cuál es la forma correcta de imprimir 'Hola, mundo!' en Python 3?",
        "options": [
            "a) print('Hola, mundo!')",
            "b) print 'Hola, mundo!'",
            "c) Console.WriteLine('Hola, mundo!')",
            "d) display('Hola, mundo!')",
        ],
        "correct": 0,
    },
    {
        "question": "¿Cuál de las siguientes es una variable booleana en Python?",
        "options": ["a) 42", "b) 'Verdadero'", "c) None", "d) True"],
        "correct": 3,
    },
    {
        "question": "¿Cuál es la función utilizada para obtener la longitud de una lista en Python?",
        "options": ["a) length()", "b) count()", "c) size()", "d) len()"],
        "correct": 3,
    },
    {
        "question": "¿Qué tipo de estructura de datos en Python almacena valores en pares clave-valor?",
        "options": ["a) Lista", "b) Conjunto", "c) Diccionario", "d) Tupla"],
        "correct": 2,
    },
    {
        "question": "¿Cuál es la palabra clave para definir una función en Python?",
        "options": ["a) def", "b) function", "c) define", "d) fun"],
        "correct": 0,
    },
    {
        "question": "¿Cuál es la forma correcta de generar una lista de números pares del 0 al 10 en Python?",
        "options": [
            "a) [x for x in range(0, 10) if x % 2 == 0]",
            "b) [x for x in range(10) if x % 2 == 0]",
            "c) [x for x in range(0, 10) where x % 2 == 0]",
            "d) [x for x in range(10) where x % 2 == 0]",
        ],
        "correct": 1,
    },
    {
        "question": "¿Qué operador se utiliza para elevar un número a una potencia en Python?",
        "options": ["a) ^", "b) **", "c) ^", "d) %"],
        "correct": 1,
    },
    {
        "question": "¿Qué método se utiliza para agregar un elemento al final de una lista en Python?",
        "options": ["a) add()", "b) push()", "c) append()", "d) insert()"],
        "correct": 2,
    },
    {
        "question": "¿Cuál es el resultado de la expresión 3 + 4 * 2 en Python?",
        "options": ["a) 10", "b) 14", "c) 11", "d) 8"],
        "correct": 1,
    },
    {
        "question": "¿Cuál de las siguientes no es una estructura de control en Python?",
        "options": ["a) if-else", "b) loop-for", "c) repeat-while", "d) while"],
        "correct": 2,
    },
    {
        "question": "¿Qué función se utiliza para obtener el valor absoluto de un número en Python?",
        "options": ["a) abs()", "b) absolute()", "c) val()", "d) absval()"],
        "correct": 0,
    },
    {
        "question": "¿Cuál es la función utilizada para leer la entrada del usuario en Python?",
        "options": ["a) input()", "b) read()", "c) get_input()", "d) user_input()"],
        "correct": 0,
    },
    {
        "question": "¿Cuál es el operador de pertenencia utilizado para verificar si un elemento está en una lista en Python?",
        "options": ["a) contains", "b) in", "c) is_in", "d) exists"],
        "correct": 1,
    },
    {
        "question": "¿Cuál de las siguientes es una manera correcta de abrir un archivo llamado 'archivo.txt' en modo lectura?",
        "options": [
            "a) open('archivo.txt', 'r')",
            "b) open('archivo.txt', 'read')",
            "c) open('archivo.txt', 'w')",
            "d) open('archivo.txt', 'write')",
        ],
        "correct": 0,
    },
    {
        "question": "¿Cuál de las siguientes es una biblioteca estándar de Python para trabajar con expresiones regulares?",
        "options": ["a) regex", "b) re", "c) regexp", "d) regx"],
        "correct": 1,
    },
    {
        "question": "¿Qué función se utiliza para encontrar el valor máximo en una lista en Python?",
        "options": ["a) max()", "b) maximum()", "c) biggest()", "d) find_max()"],
        "correct": 0,
    },
    {
        "question": "¿Cuál es la forma correcta de importar el módulo 'math' en Python?",
        "options": [
            "a) import math",
            "b) require math",
            "c) include math",
            "d) import module math",
        ],
        "correct": 0,
    },
    {
        "question": "¿Cuál de las siguientes opciones se utiliza para terminar un bucle en Python antes de que se complete su iteración?",
        "options": ["a) break", "b) end", "c) exit", "d) continue"],
        "correct": 0,
    },
    {
        "question": "¿Qué lenguaje se utiliza para definir la estructura y el contenido de una página web?",
        "options": ["a) JavaScript", "b) CSS", "c) HTML", "d) PHP"],
        "correct": 2,
    },
    {
        "question": "¿Cuál de las siguientes opciones se utiliza para aplicar estilos a elementos HTML?",
        "options": ["a) JavaScript", "b) CSS", "c) HTML", "d) SQL"],
        "correct": 1,
    },
    {
        "question": "¿Qué significa 'CSS' en diseño web?",
        "options": [
            "a) Computer Style Sheets",
            "b) Centralized Styling System",
            "c) Cascading Style Sheets",
            "d) Creative Styling System",
        ],
        "correct": 2,
    },
    {
        "question": "¿Qué se entiende por diseño web receptivo (responsive)?",
        "options": [
            "a) Diseñar un sitio web sin imágenes",
            "b) Diseñar un sitio web que solo se ve bien en dispositivos móviles",
            "c) Diseñar un sitio web que se adapta a diferentes tamaños de pantalla y dispositivos",
            "d) Diseñar un sitio web solo para navegadores modernos",
        ],
        "correct": 2,
    },
    {
        "question": "¿Cuál es la unidad de medida comúnmente utilizada para especificar tamaños de fuentes en CSS?",
        "options": [
            "a) Píxeles (px)",
            "b) Porcentajes (%)",
            "c) Pulgadas (in)",
            "d) Centímetros (cm)",
        ],
        "correct": 0,
    },
    {
        "question": "¿Qué etiqueta HTML se utiliza para enlazar a una hoja de estilo externa?",
        "options": ["a) <link>", "b) <style>", "c) <css>", "d) <stylesheet>"],
        "correct": 0,
    },
    {
        "question": "¿Qué es un 'mockup' en diseño web?",
        "options": [
            "a) Un término técnico para una animación en CSS",
            "b) Una técnica de codificación avanzada",
            "c) Un diseño visual estático que representa la apariencia de un sitio web",
            "d) Un archivo de sonido que se reproduce en un sitio web",
        ],
        "correct": 2,
    },
    {
        "question": "¿Cuál es el estándar utilizado para crear diseños de página web mediante la estructura de 12 columnas?",
        "options": ["a) Bootstrap", "b) Flexbox", "c) CSS Grid", "d) Foundation"],
        "correct": 0,
    },
    {
        "question": "¿Cuál es la paleta de colores básica en diseño web que incluye blanco, negro y todas las tonalidades de gris?",
        "options": [
            "a) Tonalidades pastel",
            "b) Gama de colores RGB",
            "c) Paleta de colores primarios",
            "d) Escala de grises",
        ],
        "correct": 3,
    },
    {
        "question": "¿Qué es un 'CMS' en diseño web?",
        "options": [
            "a) Creative Management System",
            "b) Centralized Multimedia System",
            "c) Content Management System",
            "d) Cascading Multimedia Style",
        ],
        "correct": 2,
    },
    {
        "question": "¿Cuál de las siguientes tecnologías se utiliza para animaciones y transiciones fluidas en diseño web?",
        "options": ["a) HTML", "b) CSS", "c) JavaScript", "d) PHP"],
        "correct": 1,
    },
    {
        "question": "¿Cuál es la principal característica de un diseño web minimalista?",
        "options": [
            "a) Uso excesivo de imágenes y gráficos",
            "b) Contenido sobrecargado",
            "c) Enfoque en la simplicidad y el espacio en blanco",
            "d) Uso de múltiples fuentes y colores llamativos",
        ],
        "correct": 2,
    },
    {
        "question": "¿Qué es el 'UX design' en diseño web?",
        "options": [
            "a) Uso extremo de animaciones y efectos visuales",
            "b) Enfoque en la estética visual solamente",
            "c) Diseño centrado en la experiencia del usuario",
            "d) Diseño orientado exclusivamente al contenido",
        ],
        "correct": 2,
    },
    {
        "question": "¿Qué etiqueta HTML se utiliza para crear una lista ordenada?",
        "options": ["a) <list>", "b) <ordered>", "c) <ul>", "d) <ol>"],
        "correct": 3,
    },
    {
        "question": "¿Cuál es la estructura básica de una etiqueta de enlace (hipervínculo) en HTML?",
        "options": [
            "a) <a>link</a>",
            "b) <hyperlink>URL</hyperlink>",
            "c) <a href='URL'>texto del enlace</a>",
            "d) <link>URL</link>",
        ],
        "correct": 2,
    },
    {
        "question": "¿Qué se entiende por 'scroll infinito' en diseño web?",
        "options": [
            "a) Una técnica para ocultar contenido importante",
            "b) Un diseño con una sola página sin desplazamiento",
            "c) Un efecto de desplazamiento suave",
            "d) La carga continua de contenido a medida que el usuario se desplaza",
        ],
        "correct": 3,
    },
    {
        "question": "¿Qué tipo de archivo se utiliza para agregar fuentes personalizadas a un sitio web?",
        "options": ["a) .img", "b) .font", "c) .ttf", "d) .css"],
        "correct": 2,
    },
    {
        "question": "¿Qué es 'UI design' en diseño web?",
        "options": [
            "a) User Interface Design",
            "b) Ultimate Integration Design",
            "c) Unified Interaction Design",
            "d) Unique Illustration Design",
        ],
        "correct": 0,
    },
    {
        "question": "¿Qué etiqueta HTML se utiliza para insertar una imagen en una página web?",
        "options": ["a) <img>", "b) <picture>", "c) <image>", "d) <src>"],
        "correct": 0,
    },
    {
        "question": "¿Cuál es la función del 'wireframe' en el proceso de diseño web?",
        "options": [
            "a) Optimizar imágenes para la web",
            "b) Definir la estructura y disposición de los elementos en una página",
            "c) Agregar animaciones interactivas a la página",
            "d) Generar códigos de programación automáticamente",
        ],
        "correct": 1,
    },
    {
        "question": "¿Qué es una dirección IP en el contexto de redes informáticas?",
        "options": [
            "a) Un número único que identifica una computadora o dispositivo en una red",
            "b) Un código de barras utilizado para identificar dispositivos en una red",
            "c) Un nombre de usuario utilizado para acceder a una red",
            "d) Un protocolo de enrutamiento utilizado en redes inalámbricas",
        ],
        "correct": 0,
    },
    {
        "question": "¿Qué protocolo se utiliza para enviar y recibir correos electrónicos?",
        "options": ["a) HTTP", "b) FTP", "c) SMTP", "d) DNS"],
        "correct": 2,
    },
    {
        "question": "¿Cuál es la función del protocolo DHCP en una red?",
        "options": [
            "a) Enviar correos electrónicos",
            "b) Asignar direcciones IP de forma automática a dispositivos en la red",
            "c) Gestionar la seguridad de la red",
            "d) Proporcionar servicios de almacenamiento en la nube",
        ],
        "correct": 1,
    },
    {
        "question": "¿Qué dispositivo se utiliza para conectar diferentes redes y gestionar el tráfico entre ellas?",
        "options": ["a) Hub", "b) Switch", "c) Router", "d) Modem"],
        "correct": 2,
    },
    {
        "question": "¿Qué tecnología inalámbrica permite la conexión de dispositivos a corta distancia?",
        "options": ["a) Ethernet", "b) Wi-Fi", "c) Bluetooth", "d) 4G"],
        "correct": 2,
    },
    {
        "question": "¿Cuál de las siguientes afirmaciones describe mejor una red LAN?",
        "options": [
            "a) Cubre una gran área geográfica, como una ciudad o un país",
            "b) Conecta dispositivos a nivel mundial a través de Internet",
            "c) Se limita a una ubicación geográfica, como una oficina o un hogar",
            "d) Se utiliza principalmente para la conexión de dispositivos móviles",
        ],
        "correct": 2,
    },
    {
        "question": "¿Qué protocolo se utiliza para convertir nombres de dominio en direcciones IP?",
        "options": ["a) SMTP", "b) HTTP", "c) DNS", "d) DHCP"],
        "correct": 2,
    },
    {
        "question": "¿Cuál de las siguientes opciones es una topología de red en la que todos los dispositivos están conectados en un solo circuito cerrado?",
        "options": ["a) Estrella", "b) Bus", "c) Anillo", "d) Malla"],
        "correct": 2,
    },
    {
        "question": "¿Cuál de las siguientes opciones es una dirección IP reservada para la propia máquina local?",
        "options": ["a) 127.0.0.1", "b) 192.168.1.1", "c) 10.0.0.1", "d) 172.16.0.1"],
        "correct": 0,
    },
    {
        "question": "¿Qué es un cortafuegos (firewall) en una red?",
        "options": [
            "a) Un dispositivo para aumentar la velocidad de la red",
            "b) Un dispositivo para conectarse a Internet",
            "c) Un sistema de seguridad que controla el tráfico de red entrante y saliente",
            "d) Un dispositivo para expandir la cobertura de la red",
        ],
        "correct": 2,
    },
    {
        "question": "¿Qué protocolo se utiliza para transferir archivos de una computadora a un servidor en una red?",
        "options": ["a) HTTP", "b) FTP", "c) SMTP", "d) POP3"],
        "correct": 1,
    },
    {
        "question": "¿Cuál de las siguientes opciones describe mejor una red WAN?",
        "options": [
            "a) Cubre una pequeña área geográfica, como una casa",
            "b) Conecta dispositivos en una ubicación específica, como una oficina",
            "c) Cubre una gran área geográfica, como una ciudad o un país",
            "d) Es una red inalámbrica utilizada en dispositivos móviles",
        ],
        "correct": 2,
    },
    {
        "question": "¿Cuál es el propósito del protocolo HTTPS en una conexión web?",
        "options": [
            "a) Realizar llamadas de API",
            "b) Descargar archivos grandes",
            "c) Navegar por sitios web",
            "d) Proporcionar una capa de seguridad en la transferencia de datos",
        ],
        "correct": 3,
    },
    {
        "question": "¿Cuál de las siguientes opciones es un tipo de dirección IP que cambia cada vez que se conecta a Internet?",
        "options": [
            "a) Dirección IP fija",
            "b) Dirección IP dinámica",
            "c) Dirección IP privada",
            "d) Dirección IP pública",
        ],
        "correct": 1,
    },
    {
        "question": "¿Qué es un ataque DDoS en el contexto de redes informáticas?",
        "options": [
            "a) Un ataque que roba información confidencial de una red",
            "b) Un ataque que secuestra la red y exige un rescate",
            "c) Un ataque que sobrecarga una red con tráfico malicioso desde múltiples fuentes",
            "d) Un ataque que infecta dispositivos con malware",
        ],
        "correct": 2,
    },
    {
        "question": "¿Qué protocolo se utiliza para enviar y recibir correo electrónico en un cliente de correo, como Outlook o Thunderbird?",
        "options": ["a) POP3", "b) SMTP", "c) HTTP", "d) FTP"],
        "correct": 0,
    },
    {
        "question": "¿Qué tipo de dirección IP se utiliza para identificar una máquina dentro de una red local?",
        "options": [
            "a) Dirección IP pública",
            "b) Dirección IP global",
            "c) Dirección IP privada",
            "d) Dirección IP dinámica",
        ],
        "correct": 2,
    },
    {
        "question": "¿Qué protocolo se utiliza para acceder y transferir archivos de manera remota en una red?",
        "options": ["a) HTTP", "b) FTP", "c) SMTP", "d) DNS"],
        "correct": 1,
    },
    {
        "question": "¿Cuál es el propósito principal de un switch en una red?",
        "options": [
            "a) Establecer conexiones entre redes diferentes",
            "b) Administrar la seguridad de la red",
            "c) Conectar dispositivos en una red local y gestionar el tráfico",
            "d) Proporcionar acceso a Internet",
        ],
        "correct": 2,
    },
    {
        "question": "¿Qué es NAT (Network Address Translation)?",
        "options": [
            "a) Una técnica para mejorar la velocidad de la red",
            "b) Un protocolo de seguridad avanzado",
            "c) Un enrutador de alta velocidad",
            "d) Una técnica para asignar direcciones IP privadas a direcciones IP públicas",
        ],
        "correct": 3,
    },
]

preguntas = Label(
    root, text="Questions", wraplength=750, font=("Helvetica", 25, "bold")
)
preguntas.pack(pady=20)

respuestas = []
for i in range(4):
    boton = Button(
        root,
        text="Answers",
        command=lambda i=i: checkar_preguntas(i),
        height=3,
        width=40,
        font=("Helvetica", 12),
        bg="black",
        fg="white",
        relief="sunken",
        cursor="hand2",
    )
    boton.pack(pady=5)
    respuestas.append(boton)

oportunidades = 2
pregunta_actual = 0
intentos = 0
puntos = 0
record = 0

etiqueta_puntos = Label(
    root, text="Puntos", font=("Helvetica", 20, "bold"), fg="red", bg="black"
)
etiqueta_puntos.pack(anchor="nw", padx=20, pady=2)

contador = Label(
    root, text="Preguntas", font=("Helvetica", 20, "bold"), fg="brown", bg="black"
)
contador.pack(anchor="center", padx=10, pady=2)

registro = Label(
    root, text="Record", font=("Helvetica", 35, "bold"), fg="green", bg="black"
)
registro.pack(anchor="se", padx=20, pady=2)


def cargar_preguntas():
    global intentos
    if pregunta_actual < len(questions):
        datos_preguntas = questions[pregunta_actual]
        preguntas.config(text=datos_preguntas["question"])

        for i in range(4):
            respuestas[i].config(text=datos_preguntas["options"][i])

        intentos = 0
        contador.config(text=f"Pregunta: {pregunta_actual+1}/{len(questions)}")
        etiqueta_puntos.config(text=f"Puntos: {puntos}/1000")
        registro.config(text=f"Record: {record}")


def checkar_preguntas(selected):
    global pregunta_actual, oportunidades, intentos, puntos, record

    datos_preguntas = questions[pregunta_actual]
    respuesta_correcta = datos_preguntas["correct"]
    intentos += 1

    if selected == respuesta_correcta:
        if intentos == 1:
            puntos += 10
        elif intentos == 2:
            puntos += 5

        pregunta_actual += 1
        oportunidades = 2

        if puntos > record:
            record = puntos

        if pregunta_actual < len(questions):
            cargar_preguntas()
        else:
            messagebox.showinfo(
                "Fin del juego",
                f"¡Has respondido todas las preguntas correctamente! Puntaje total: {puntos} puntos",
            )
            fin = messagebox.askquestion("De nuevo", "¿Quieres superar tu record?")
            if fin == "yes":
                puntos = 0
                pregunta_actual = 0
                cargar_preguntas()
            else:
                root.destroy()

    else:
        oportunidades -= 1
        if oportunidades > 0:
            messagebox.showinfo(
                "Incorrecto",
                f"Respuesta incorrecta. Te queda {oportunidades} oportunidad.",
            )
        else:
            messagebox.showinfo(
                "Sin oportunidades",
                f"¡Perdiste todas las oportunidades! Volviendo a la pregunta 1. Puntaje total: {puntos}",
            )
            oportunidades = 2
            puntos = 0
            pregunta_actual = 0
            cargar_preguntas()


cargar_preguntas()
root.mainloop()