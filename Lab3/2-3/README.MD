# LAB 3-2 y 3-3: Implementación de un Data Warehouse con BigQuery

| Información |  |
| --- | --- |
| Materia | Tópicos especiales en Telemática |
| Curso | ST0263 |
| Estudiante | Antonio Carmona Gaviria (acarmonag@eafit.edu.co) |
| Profesor | Edwin Nelson Montoya Munera (emontoya@eafit.edu.co) |

## 1. Objetivo

El propósito principal es establecer un Data Warehouse utilizando BigQuery.

## 2. Aspectos Resueltos

- Creación de un bucket en GCP Cloud Storage: Completado.
- Carga de datos al bucket de Cloud Storage: Completado.
- Configuración de un dataset y una tabla en BigQuery: Completado.
- Inferencia automática del esquema de datos en Cloud Storage: Completado.
- Ejecución de consultas SQL en BigQuery a los datos de Cloud Storage: Completado.

## 5. Ambiente de Ejecución

### Guía de Uso

#### Parte 1: Preparativos Iniciales

1. Descarga del archivo '[data.zip](https://github.com/spuertaf/spuertaf-st0263/blob/main/Lab3-2y3-3/data.zip)' y extracción de su contenido.
   
   

#### Parte 2: Crear un Bucket en GCP Cloud Storage

1. Acceder a 'Cloud Storage' en la consola de GCP.
2. Usar el botón 'CREAR' en la sección 'Buckets'.
   

3. Nombrar el bucket y configurarlo para la región 'us-central1 (Iowa)'.
   

4. Finalizar la creación del bucket.
   
   **Resultado:** Bucket en GCP Cloud Storage creado exitosamente.

#### Parte 3: Carga de Datos al Bucket

1. Navegar al bucket creado en Cloud Storage.
2. Usar 'SUBIR ARCHIVOS' para cargar las particiones de datos descomprimidas previamente.

   **Resultado:** Datos cargados exitosamente en el bucket.

#### Parte 4: Configuración de Dataset y Tabla en BigQuery

1. Abrir 'Big Query' en la consola de GCP.
2. Crear un nuevo conjunto de datos (dataset) desde el menú del proyecto.
   

3. Nombrar el dataset y configurarlo para la misma región del bucket.
4. Crear una nueva tabla en el dataset recién creado.
5. Elegir 'Google Cloud Storage' como fuente y seleccionar un archivo del bucket.


6. Utilizar un patrón con asterisco (*) para referenciar todos los archivos del bucket.
   

7. Nombrar la tabla y elegir 'Tabla externa' como tipo.
8. Habilitar la detección automática del esquema.
   
   **Resultado:** Tabla en BigQuery vinculada a datos de Cloud Storage creada con éxito.

#### Parte 5: Autoinferencia de Esquema en BigQuery

1. Revisar el esquema inferido automáticamente por BigQuery en la tabla creada.
   

   **Observación:** BigQuery identifica automáticamente el esquema de los datos.

#### Parte 6: Ejecución de Consultas SQL en BigQuery

1. En BigQuery, seleccionar el conjunto de datos y la tabla creados anteriormente.
2. Acceder a la opción 'CONSULTA' y abrir una nueva pestaña de consulta.
3. Realizar una consulta SQL a la tabla con el comando proporcionado:
   
   ```sql
   SELECT * FROM `su_proyecto.su_conjunto_de_datos.su_tabla`;
   ```

   Ejemplo de consulta a la tabla creada:

   ```sql
   SELECT * FROM `telematics-challenges.oline_retail_dataset.retail_table`;
   ```


   **Resultado:** Capacidad para realizar consultas SQL a través de BigQuery establecida.

Con estos pasos, se logra la implementación efectiva de un Data Warehouse utilizando BigQuery, desde la creación de un bucket en Cloud Storage hasta la ejecución de consultas SQL en los datos almacenados.