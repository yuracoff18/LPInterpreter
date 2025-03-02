# LPInterpreter

### Yura Hernandez

## Explicacion parte A
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

## Explicacion parte B
En esta parte contamos con 2 funciones y importamos las funciones de la parte A (val y string_to_list) junto con el diccionario values  

### Funcion prove_val: 
**Entrada: Lista con elementos de logica proposicional (LP)**  
**Salida: int**  
Esta funcion se encarga de evaluar si la expresion dada es una tautologia, una contradiccion o una contingencia por metodo de fuerza bruta.

**_Explicacion detallada_**:  
Esta funcion tendra ciclos anidados para cada atomo (Ya pre establecidos) y probara cada uno de sus valores de verdad mediante la funcion ya creada en la parte A (funcion val), almacenando estos valores en una lista. Cuando ya haya provado todos los valores, se hara un conteo de los valores retornados. En caso de que se encuentren solo unos (1) se devolvera 1 mostrando que es una tautologia, si solo encuentra ceros (0) devolvera 0 mostrando que es una contradiccion, pero si encuentra unos y ceros (1 y 0) se devolvera -1 mostrando que es una contingencia.


### Funcion main:
La funcion main se encarga de leer los datos de entrada y llamar la funcion prove_val.