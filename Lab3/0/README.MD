# LAB 3-0: Creación de un Clúster EMR

| Información |  |
| --- | --- |
| Materia | Tópicos especiales en Telemática |
| Curso | ST0263 |
| Estudiante | Antonio Carmona Gaviria (mailto:spuertaf@eafit.edu.co) |
| Profesor | Edwin Nelson Montoya Munera (mailto:emontoya@eafit.edu.co) |

# 1. Objetivo

Creación de un Clúster AWS EMR en Amazon para trabajar todos los laboratorios.

---

# 2. Aspectos solucionados y no solucionados

- [x]  Creación de un par de claves.
- [x]  Creación de un bucket de AWS S3 para almacenar los notebooks que crearemos en el clúster de AWS EMR.
- [x]  Creación de un Clúster AWS EMR versión 6.14.0
- [x]  Conexión por medio de SSH con el nodo maestro.
- [x]  Servicio Hue funcional.
- [x]  Servicio JupyterHub funcional.

---
# Ambiente de Ejecución y Guía Paso a Paso

Esta guía detalla el proceso para establecer un Clúster AWS EMR, indispensable para desarrollar los laboratorios del curso. Se detalla a continuación los pasos necesarios para su correcta implementación.

## Parte 1: Creación de un Par de Claves

Primero, es necesario crear un par de claves en AWS para garantizar el acceso seguro al clúster. Para esto, siga estos pasos:

1. Acceda a AWS y busque el servicio EC2.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/1.png)
2. En el panel de EC2, haga clic en ‘Pares de claves’.
3. Elija la opción ‘Crear pares de claves’.
4. Asigne un nombre al par de claves y cree el par.
5. Guarde el par de claves descargado en su computadora.

## Parte 2: Configuración de un Bucket de AWS S3

Continúe con la creación de un bucket en AWS S3, que servirá para almacenar notebooks del clúster:

1. Ingrese al servicio S3 desde la consola de AWS.
2. Haga clic en ‘Crear bucket’.
3. Asigne un nombre al bucket, mantenga las configuraciones por defecto y cree el bucket.

## Parte 3: Implementación del Clúster AWS EMR (Versión 6.14.0)

Ahora, proceda a crear el Clúster AWS EMR:

1. Desde la consola de AWS, acceda al servicio EMR.
2. Seleccione ‘Crear clúster’.
3. Nombre el clúster, elija la versión ‘emr-6.14.0’ y opte por ‘Custom’.
4. En ‘Paquete de Aplicaciones’, elija las aplicaciones requeridas y active las opciones para Hive y Spark.
5. Configure los nodos (principal, centrales y de tareas) con instancias ‘m5.xlarge’.
6. En ‘Terminación del clúster’, establezca un tiempo de inactividad de 3 horas.
7. En ‘Configuración de software’, ingrese la configuración específica para el bucket de S3 creado anteriormente.
8. En ‘Configuración de seguridad y par de claves de EC2’, seleccione el par de claves creado en la Parte 1.
9. En ‘Roles de IAM’, asigne los roles ‘EMR_DefaultRole’, ‘EMR_EC2_DefaultRole’ y ‘LabRole’ respectivamente.
10. Finalice creando el clúster.

## Parte 4: Configuración de los Puertos

Es esencial abrir los puertos necesarios para las aplicaciones:

1. En la consola de AWS, vaya a EMR y seleccione el clúster en estado ‘Esperando’.
2. En ‘Bloquear el acceso público’, desactive esta opción.
3. En ‘Aplicaciones’, anote los puertos TCP que deben estar abiertos.
4. En el servicio EC2, abra los puertos TCP indicados en las reglas de entrada del grupo de seguridad del clúster.

## Parte 5: Acceso SSH al Nodo Maestro

Para conectar al nodo maestro del clúster:

1. En EMR, seleccione su clúster y acceda a la opción de conexión SSH.
2. Siga las instrucciones proporcionadas para establecer la conexión SSH.
3. Una vez conectado, edite el archivo ‘hue.ini’ para ajustar el puerto de webhdfs y reinicie el servicio Hue.

## Parte 6: Uso de Hue

Para gestionar archivos en Hue:

1. En el servicio EMR, seleccione su clúster y vaya a ‘Aplicaciones’.
2. Acceda a Hue usando el URL proporcionado y registre un usuario y contraseña.

## Parte 7: Utilización de JupyterHub

Finalmente, para trabajar con JupyterHub:

1. En EMR, acceda a ‘Aplicaciones’ y elija JupyterHub.
2. Ingrese con las credenciales proporcionadas y cree un nuevo notebook de PySpark.
3. Verifique que las variables de contexto de Spark estén configuradas.

Con estos pasos, tendrá un clúster EMR listo para utilizar en los laboratorios del curso.