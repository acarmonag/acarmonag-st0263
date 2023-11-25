# LAB 3-1: Gestión de Archivos en HDFS y S3

| Información |  |
| --- | --- |
| Materia | Tópicos especiales en Telemática |
| Curso | ST0263 |
| Estudiante | Antonio Carmona Gaviria (acarmonag@eafit.edu.co) |
| Profesor | Edwin Nelson Montoya Munera (emontoya@eafit.edu.co) |


## 1. Objetivo

El objetivo de este laboratorio es copiar todos los archivos disponibles en el repositorio [ Datasets](https://github.com/st0263eafit/st0263-232/tree/main/bigdata/datasets) a dos sistemas de almacenamiento distintos: HDFS, que se utiliza para almacenamiento temporal, y S3, empleado para almacenamiento permanente.

## 2. Aspectos Solucionados y No Solucionados

Se lograron los siguientes objetivos:

- Crear un bucket público en AWS S3.
- Gestionar archivos en HDFS a través de la terminal.
- Manejar archivos en HDFS mediante la interfaz de HUE.
- Administrar archivos en S3 utilizando HUE.

## 5. Ambiente de Ejecución

### Guía de Uso

#### Parte 1: Creación de un Bucket Público en AWS S3

1. **Acceso a AWS S3:** Ingresar a la consola de AWS, buscar el servicio S3 y seleccionar la opción 'Crear bucket'.
2. **Configuración del Bucket:** Asignar un nombre único al bucket. En la sección 'Object Ownership', activar 'ACLs enabled' y marcar la casilla 'Object writer'. En 'Block Public Access settings for this bucket', desactivar la opción 'Block all public access' y aceptar las advertencias sobre la configuración de acceso público.
   
   ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/1/IMGS/1.png)
   ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/1/IMGS/2.png)
   ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/1/IMGS/3.png)

3. **Creación del Bucket:** Dejar las opciones restantes por defecto y finalizar la creación del bucket con el botón correspondiente.
   
   ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/1/IMGS/4.png)
   ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/1/IMGS/5.png)


4. **Configuración de Permisos:** En el menú de S3, abrir el bucket creado y, en la sección 'Permissions', editar 'Access control list (ACL)'. Activar las casillas 'List' y 'Read' para 'Everyone (public access)' y 'Authenticated users group'. Aceptar los términos y guardar los cambios.

   ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/1/IMGS/6.png)

5. **Carga de Archivos:** Ir al enlace [ airlines](https://github.com/st0263eafit/st0263-232/blob/main/bigdata/datasets/airlines.csv), descargar el archivo y cargarlo en el bucket.


6. **Verificación de Acceso Público:** Copiar la URL del objeto en S3, eliminando la parte '/airlines.csv' del final, y verificar el acceso público en el navegador.

7. **Comandos CLI para AWS:** Se puede usar el comando `aws s3 ls s3://nombre-del-bucket` para listar los contenidos del bucket desde la CLI.

   ```bash
   aws s3 ls s3://datasetsspuertaf
   ```

#### Parte 2: Gestión de Archivos en HDFS vía Terminal

1. **Preparación de Archivos:** Descargar y descomprimir 'datasets.zip'.
2. **Creación de Clúster AWS EMR:** Seguir la guía 'Creación de un Clúster EMR' para configurar el clúster.
3. **Conexión SSH al Clúster:** Usar SSH para conectarse al clúster EMR.
4. **Creación de Directorios en HDFS:** Usar comandos para crear directorios '/user/hadoop/datasets' y '/user/hadoop/datasets/gutenberg-small' en HDFS.

   ```bash
   hdfs dfs -mkdir /user/hadoop/datasets
   hdfs dfs -mkdir /user/hadoop/datasets/gutenberg-small
   ```

5. **Transferencia de Archivos a HDFS:** Mover los archivos descomprimidos de 'gutenberg-small' al directorio creado en HDFS.

   ```bash
   hdfs dfs -put /ruta/local/gutenberg-small/*.txt /user/hadoop/datasets/gutenberg-small/
   ```

#### Parte 3: Gestión de Archivos en HDFS vía HUE

1. **Acceso a HUE:** Ingresar a la consola AWS EMR, seleccionar el clúster y acceder a HUE usando las credenciales apropiadas.
2. **Creación de Directorios en HDFS desde HUE:** Utilizar la interfaz de HUE para

 crear directorios necesarios en HDFS.
3. **Carga de Archivos desde HUE:** Subir archivos locales al directorio creado en HDFS utilizando las herramientas de HUE.

#### Parte 4: Gestión de Archivos en S3 vía HUE

1. **Navegación en HUE hacia S3:** Dentro de la interfaz de HUE, seleccionar la sección de S3.
2. **Selección de Bucket y Carga de Archivos:** Elegir el bucket creado y utilizar la opción de carga de archivos para subir documentos desde la interfaz de HUE.

**Conclusión:** La guía proporciona instrucciones detalladas para la gestión de archivos en HDFS y S3, abarcando tanto métodos de línea de comandos como interfaces gráficas como HUE, y la configuración de un bucket público en AWS S3.