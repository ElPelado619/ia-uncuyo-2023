# TP6: CSP

- Hecho por: Agustín Yornet
- Legajo: 13921

## Formulación CSP para Sudoku

- Variables: $X = conjuntoDeCeldas = \{X_1,...,X_n\}$
- Dominio: $D = \{1,2,3,4,5,6,7,8,9 \}$
- Restricciones: $C = \{C_1,C_2,C_3\}$, donde:
    - $C_1$: Un dígito $D_n$ no puede aparecer más de una vez en una fila.
    - $C_2$: Un dígito $D_n$ no puede aparecer más de una vez en una columna.
    - $C_3$: Un dígito $D_n$ no puede aparecer más de una vez en una región.

## Solución del Ejercicio 2
> Utilizar el algoritmo AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignación parcial $\{WA=red, V=blue\}$ para el problema del colorear el mapa de Australia.

![Alt text](AC3.png)

El resultado de AC-3 es falso, debido a que el dominio de NSW se encuentra vacío y, por lo tanto, una inconsistencia ha sido encontrada.

La imagen, hecha en draw.io, ilustra las primeras iteraciones del algoritmo, y momentos para los cuales ningún valor $y$ del dominio de una ciudad $Y$ permite a $(x,y)$, siendo $x$ un valor dado del dominio de una ciudad $X$, satisfacer la restricción binaria $X!=Y$. En esas iteraciones, se van eliminando valores del dominio de $X$, y en el momento que una ciudad $X$ se queda sin valores en su dominio, se encuentra una inconsistencia, porque ninguna variable $X$ puede quedarse sin valores en su dominio.
