# Combinaciones únicas

Este pequeño código permite generar un archivo de texto con las combinaciones únicas que se pueden obtener a partir de una lista de datos.

La lista de nombre `datos` contiene los datos a combinar sin que estos se repitan.

Como ejemplo, a `datos` se le asignan `variable1, variable2, variable3, variable4`. Lo que nos daría 15 posibles combinaciones:

- variable1
- variable2
- variable3
- variable4
- variable1, variable2
- variable1, variable3
- variable1, variable4
- variable2, variable3
- variable2, variable4
- variable3, variable4
- variable1, variable2, variable3
- variable1, variable2, variable4
- variable1, variable3, variable4
- variable2, variable3, variable4
- variable1, variable2, variable3, variable4

## Matemática
La fórmula matemática para calcular el número de combinaciones posibles a partir de un conjunto de elementos dados representa mediante el símbolo "C". La fórmula general para calcular el número de combinaciones de "n" elementos tomados de "r" en r se define como:
$$C_{(n,r)}=\frac{n!}{(r!*(n - r)!)}$$

Donde:
- `n` es el número total de elementos en el conjunto.
- `r` es el número de elementos que se seleccionan para cada combinación.

### _Ejemplo_

En el ejemplo, tendríamos que:
$$C_{(4,r)}=\frac{4!}{(r!*(4 - r)!)}$$

`r` sería entonces el número de elementos en cada combinación. En este ejemplo tenemos 4 variables, por ende tenemos combinaciones de 1, 2, 3 y 4.
- Combinaciones de 1: $$C_{(4,1)}=\frac{4!}{(1!*(4 - 1)!)}=4$$
- Combinaciones de 2: $$C_{(4,2)}=\frac{4!}{(2!*(4 - 2)!)}=6$$
- Combinaciones de 3: $$C_{(4,3)}=\frac{4!}{(3!*(4 - 3)!)}=4$$
- Combinaciones de 4: $$C_{(4,4)}=\frac{4!}{(4!*(4 - 4)!)}=1$$

La suma de los resultados nos da `15`. En total, son `15` posibles combinaciones sin repeticiones.

_Para 11 datos en `datos`, el total de combinaciones sería de 2047, por dar otro ejemplo._

## ¿Para qué?
En mi caso, lo uso para saber las condicionales ```if``` que necesito. Por ejemplo, si necesito inyectar datos de forma dinámica a una base de datos.

Es decir, tengo 4 campos que pueden o no recibir datos. A partir de los datos que recibamos, generaremos la SQL query que será ejecutada para inyectar los datos. Así que será importante saber las combinaciones posibles para programar los ```if``` necesarios.

Aclarando que en algunas ocaciones usar condicionales ```if``` es la opción más óptima. En otras, con un ```switch/case``` será más eficiente y más limpio el código.

Usando el ejemplo anterior:
- Si me dan variable1 y no las demás:
```php
if(variable1 && !variable2 && !variable3 && !variable4) {
    //hacemos algo...
}
```
- Si me dan variable3 y variable4 y no las demás:
```php
if(!variable1 && !variable2 && variable3 && variable4) {
    //hacemos algo...
}
```
Este pequeño programa en Python me ayuda a saber las combinaciones y por ende los `if` necesarios.
¿Habrá alguna forma más eficiente de hacer lo anterior? Seguramente, pero solo es un ejemplo del uso que le doy al código.
