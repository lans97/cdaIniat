# cdaIniat
Pequeña parte del proyecto de calidad del aire para el INIAT

## TODOS

- ~~Completar wrapper de base de datos~~
- ~~Investigar API para cambiar a actualización por eventos~~ (equivocaición verbal del técnico)
- ~~Integrar sitios con base de datos~~
- ~~Investigar API de telegram para hacer un bot~~

## Notas

Los tokens de cada sensor se guardan localmente en el archivo sensors.py, no se suben al repositorio por seguridad.

## 20/02/2024

### TODO
- ~~Wrapper API smability~~

### Notas
- Mini wrapper seguro terminado

## Descripción

Pequeño programa para la sincronización de base de datos de Smability con una base de datos local.

Se utilizó el ORM sqlalchemy para el manejo de la base de datos. (https://docs.sqlalchemy.org/en/20/)

No recomiendo almacenar la información de manera local si se tiene acceso a la API de Smability.
Sin embargo, si es necesario sincronizar, recomiendo realizar un programa que
pueda sincronizar bloques grandes de datos y verifique si se tiene la información
de manera local. Una el wrapper de la API de smability debería ayudar con eso.
también recomiendo hacer una copia de los campos que devuelve la API de Smability
para mejor compatibilidad.

### Archivos

#### db.sql
Descripción de la base de datos actual.

#### orm.py
Declaración de clases para el ORM y su interacción con la base de datos.

#### smability.py
Wrapper de la API de Smability. Proporciana logging y manejo de excepciones
básicas para evitar romper el flujo del programa.

#### setup.py
Ejecuta funciones para incicialización de base de datos y ORM.

#### main.py
Realiza la sincronización cada 5 minutos.
