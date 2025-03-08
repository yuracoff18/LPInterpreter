# LPInterpreter

### Yura Hernandez

## _Explicacion parte A_ **Collazos**
En esta parte contamos con tres funciones y dos diccionarios globales.

**Los diccionarios son:**  
values  
op  

### Diccionario values:
Este diccionario guardará los valores de verdad para cada atomo asignado al inicio del programa.  

### Diccionario op (Operators):
Este diccionario guarda los simbolos de & y | junto con su funcion.  

**Las funciones son:**  
String_to_list   
val  
main  


### Funcion string_to_list:
**Entrada: String**  
**Salida: Lista**  
Esta funcion recibe un string y devuelve una lista sin contar los espacios.  
  
  
### Funcion val:  
**Entrada: Lista a evaluar, indice de comienzo, indice del final**  
**Salida: Bool**  
Esta funcion evalua una lista con elementos de la logica proposicional y devuelve su valor de verdad.

**_Explicacion detallada_**:
La funcion val es una funcion recursiva (Se llama a si misma) recibe de entrada una lista con los elementos de una expresion de logica proposicional, un indice de comienzo y un indice final. 

La funcion comienza evaluando si el indice de inicio y final es igual, si es asi, devolvera el valor de verdad asignado a este atomo, si no es asi verificara si  el indice de inicio es un operador __not (!)__, si lo es, la funcion se llamara a si misma negando el valor que regrese, de lo contrario si el valor de inicio es un __parentesis abierto__ y el valor de final es un __parentesis cerrado__ se iniciara un ciclo desde el valor de indice inicial mas (+) uno (1) hasta el final, buscando un operador logico __(Valor en diccionario op)__ en medio de la expresion (sin parentesis de por medio). 

Una vez haya encontrado el operador logico en el medio de la operacion se almacenara el indice en la variable lop **(logical operator)** y se evaluaran los resultados de las expresiones por medio de diccionarios teniendo como entradas a la funcion val, la funcion val tendra de entradas las siguientes:  

Expresion de la izquierda:  
Lista completa con los elementos de logica porpocicional **(LP)**, valor de indice inicial mas uno **(start + 1)**, valor de indice del operador del medio menos 1 **(lop - 1)**

Expresion de la derecha:
Lista completa con los elementos de logica porpocicional **(LP)**, valor de indice del operador del medio mas uno **(lop + 1)**, valor del indice final menos 1 **(end - 1)**  

Esto evaluara las expresiones internas de la expresion principal, volviendo a la evaluacion inicial.

### Funcion main:
La funcion main se encarga de leer los datos de entrada y establecer los valores de verdad para cada atomo en la expresion de logica proposicional.  


## _Explicacion parte A_ **Yura**
En esta parte contamos con 4 funciones, dos diccionarios globales y una clase.  

**Los diccionarios son:**  
values  
op  

### Diccionario values:
Este diccionario guardará los valores de verdad para cada atomo asignado al inicio del programa.  

### Diccionario op (Operators):
Este diccionario guarda los simbolos de & y | junto con su funcion. 


### Clase node
**La clase node cuenta con 3 atributos:**  
- right  
- center  
- left  
  
y un metodo llamado **true_value**  
- Lo que hace es evaluar lo que se tiene al lado izquierdo y derecho con el operador que esta situado en el centro.


### Funcion no_space_str:  
**Entrada: str**  
**Salida: str**   
Esta funcion recibe un string con espacios y lo devuelve sin ellos. 



### Funcion valid_LP:
**Entrada: LP**  
**Salida: bool**  
Esta funcion recibe la expresion de logica proposicional y la evalua usando el metodo de pila, adicioné como requisito que en los parentesis haya un operador en la mitad.


### Funcion val:
**Entrada: LP, start, end**  
**Salida: bool**  
  
La funcion separa la expresion de logica proposicional dependiendo de su punto de partida, comenzando con el operador negacion y luego con el operador en el medio, para luego  devolver el valor de verdad de toda la expresion.

**_Explicacion detallada_**:
La funcion val recibe como entrada una expresion de logica proposicional, su posicion inicial y su posicion final. Primero se evalua que hay en su posicion inicial, si es un signo de not **(!)** negara todo lo que hay al frente de el entrando otra vez a la misma funcion pero con el punto de partida con un mas uno **(+1)** y activando la flag negation para saltar el siguiente proceso. Si el punto de partida no es un operador not comenzara el proceso de encontrar el indice del operador central, y una vez lo haya encontrado se creara un nodo el cual tendra en su lado izquierdo el valor de la expresion logica desde el punto inicial hasta el valor de la posicion del operador central menos uno **(-1)**, en la posicion central se pondra el operador y al lado derecho tendra el valor de la expresion logica desde la posicion del operador central mas uno **(+1)** hasta el final. Una vez creado el nodo dependiendo de si la expresion que se encuentra en los extremos es un atomo se convertira en su valor de verdad, si no la expresion entrará otra vez a la funcion val. Una vez haya vuelto, la variable ans tomara el valor del metodo **true_value** y lo retornará.


### Funcion main:
La funcion main se encarga de leer los datos y recibir el valor de la funcion **valid_LP** para continuar con la evaluacion de las expresiones de logica proposicional.


## _Explicacion parte B_
En esta parte contamos con 2 funciones y importamos las funciones de la parte A (val y string_to_list) junto con el diccionario values  

### Funcion prove_val: 
**Entrada: Lista con elementos de logica proposicional (LP)**  
**Salida: int**  
Esta funcion se encarga de evaluar si la expresion dada es una tautologia, una contradiccion o una contingencia por metodo de fuerza bruta.

**_Explicacion detallada_**:  
Esta funcion tendra ciclos anidados con una lista de o y 1, alternando asi para cada atomo (atomos ya pre establecidos) y probara cada uno de sus valores de verdad mediante la funcion ya creada en la parte A (funcion val), almacenando estos valores en una lista. Cuando ya haya probado todos los valores, se hara un conteo de los valores retornados. En caso de que se encuentren solo unos (1) se devolvera 1 mostrando que es una tautologia, si solo encuentra ceros (0) devolvera 0 mostrando que es una contradiccion, pero si encuentra unos y ceros (1 y 0) se devolvera -1 mostrando que es una contingencia.


### Funcion main:
La funcion main se encarga de leer los datos de entrada y llamar la funcion prove_val.