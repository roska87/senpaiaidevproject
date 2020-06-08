# Proyecto GAN Condicional
Senpai Academy - AI Developer 

### Descripción de la problemática
La idea del proyecto es crear una red GAN Condicional, 
donde a partir de una etiqueta, la red genere una imágen correspondiente a la misma.

### Descripción de la solución inicial

<ul>
    <li>Inicialmente la idea es utilizar un dataset conocido para asegurar el funcionamiento del mismo en la red a desarrollar.</li> 
    <li>Se tomaría el dataset CIFAR10 de Keras, el mismo ya contiene imágenes con sus etiquetas correspondientes.</li>
    <li>Crear una red Generadora que reciba ruido y una etiqueta.</li>
    <li>Crear una red Discriminadora que reciba una imágen y una etiqueta.</li>
    <li>La red GAN combinaría el funcionamiento de la red generadora y la red Discriminadora.</li>
    <li>Iterar sobre la solución desarrollada para lograr la mayor presición posible.</li>
    <li>Después de comprobar el funcionamiento de la red con el dataset CIFAR10, crear un nuevo dataset para entrenar nuevamente la red y probarlo sobre esta nueva.</li>
</ul>

### Descripción inicial del algoritmo

El algoritmo para entrenar la red GAN sería compuesto por los siguientes puntos:

<ol>
    <li>Carga del dataset.</li>
    <li>Normalización de las imágenes.</li>
    <li>Creación de modelo Generador el cual recibiría ruido junto con una etiqueta y retornaría una imágen.</li>
    <li>Creación de modelo Discriminador, el cual recibe una imágen y una etiqueta, y retorna si la imágen y su etiqueta son verdaderas o falsas.</li>
    <li>Creación de modelo GAN, el cual combina al Generador y Discriminador; de esta forma, recibiría ruido y una etiqueta, y retorna si lo generado en el proceso es verdadero o falso.
        Para el mismo, se concatenan los modelos previos, pasando el Generador como entrada del Discriminador.</li>
    <li>Se pre entrena el Discriminador, para dar cierta ventaja contra el Generador y así en el entrenamiento posterior obligar a este a realizar ¨mejoras¨ en sus resultados para poder engañar al Discriminador.<li>
    <li>Posteriormente, se pasa a entrenar la red GAN, donde se alterna la posibilidad de entrenar los pesos de ambas redes; Se generan imágenes falsas con el Generador a partir de ruido y una etiqueta. Las imágenes generadas, junto con mas del dataset, se utilizan para entrenar al Discriminador.
        Por último, congelando los pesos del Discriminador, se entrena el Generador a traves del modelo GAN.</li>
    <li>Los pasos mencionados en el punto anterior, serían realizados en cada epoch, guardando la pérdida de ambas redes para poder visualizar el avance del entrenamiento.</li>    
</ol>

### Visualización de la arquitectura de la red GAN Condicional

![alt text](/images/cGAN.png)