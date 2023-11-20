# LAB 3-0: Creación de un Clúster EMR

| Información |  |
| --- | --- |
| Materia | Tópicos especiales en Telemática |
| Curso | ST0263 |
| Estudiante | Antonio Carmona Gaviria (acarmonag@eafit.edu.co) |
| Profesor | Edwin Nelson Montoya Munera (emontoya@eafit.edu.co) |

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
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/2.png)
3. Elija la opción ‘Crear pares de claves’.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/3.png)
4. Asigne un nombre al par de claves y cree el par.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/4.png)
5. Guarde el par de claves descargado en su computadora.

## Parte 2: Configuración de un Bucket de AWS S3

Continúe con la creación de un bucket en AWS S3, que servirá para almacenar notebooks del clúster:

1. Ingrese al servicio S3 desde la consola de AWS.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/5.png)
2. Haga clic en ‘Crear bucket’.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/6.png)
3. Asigne un nombre al bucket, mantenga las configuraciones por defecto y cree el bucket.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/7.png)
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/8.png)

## Parte 3: Implementación del Clúster AWS EMR (Versión 6.14.0)

Ahora, proceda a crear el Clúster AWS EMR:

1. Desde la consola de AWS, acceda al servicio EMR.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/9.png)
2. Seleccione ‘Crear clúster’.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/10.png)
3. Nombre el clúster, elija la versión ‘emr-6.14.0’ y opte por ‘Custom’.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/11.png)
4. En ‘Paquete de Aplicaciones’, elija las aplicaciones requeridas y active las opciones para Hive y Spark.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/12.png)
5. Configure los nodos (principal, centrales y de tareas) con instancias ‘m5.xlarge’.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/13.png)
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/14.png)
6. En ‘Terminación del clúster’, establezca un tiempo de inactividad de 3 horas.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/15.png)
7. En ‘Configuración de software’, ingrese la configuración específica para el bucket de S3 creado anteriormente.
    configuración:
    
    ```json
    [
      {
        "Classification": "jupyter-s3-conf",
        "Properties": {
          "s3.persistence.enabled": "true",
          "s3.persistence.bucket": "nombre_bucket_creado_en_paso2"
        }
      }
    ]
    ```
    
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/16.png)
8. En ‘Configuración de seguridad y par de claves de EC2’, seleccione el par de claves creado en la Parte 1.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/17.png)
9. En ‘Roles de IAM’, asigne los roles ‘EMR_DefaultRole’, ‘EMR_EC2_DefaultRole’ y ‘LabRole’ respectivamente.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/18.png)
10. Finalice creando el clúster.

## Parte 4: Configuración de los Puertos

Es esencial abrir los puertos necesarios para las aplicaciones:

1. En la consola de AWS, vaya a EMR y seleccione el clúster en estado ‘Esperando’.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/19.png)
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/20.png)
2. En ‘Bloquear el acceso público’, desactive esta opción.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/21.png)
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/22.png)
3. En ‘Aplicaciones’, anote los puertos TCP que deben estar abiertos.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/23.png)
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/24.png)
4. En el servicio EC2, abra los puertos TCP indicados en las reglas de entrada del grupo de seguridad del clúster.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/25.png)
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/26.png)
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/27.png)
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/28.png)
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/29.png)
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/30.png)

## Parte 5: Acceso SSH al Nodo Maestro

Para conectar al nodo maestro del clúster:

1. En EMR, seleccione su clúster y acceda a la opción de conexión SSH.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/31.png)
2. Siga las instrucciones proporcionadas para establecer la conexión SSH.
3. Una vez conectado, edite el archivo ‘hue.ini’ para ajustar el puerto de webhdfs y reinicie el servicio Hue.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/32.png)
3.1. Escriba el siguiente comando en la terminal:
        
    ```bash
    sudo nano /etc/hue/conf/hue.ini
    ```

3.2. Busque la linea que contenga ‘webhdfs_url’ y cambiar el puerto de 14000 a 9870:
![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/33.png)

3.3. Presione las teclas control + X y Y + enter, para guardar los cambios.

3.4. Reinicie el servicio Hue mediante el siguiente comando:
            
    ```bash
    sudo systemctl restart hue.service
    ```

## Parte 6: Uso de Hue

Para gestionar archivos en Hue:

1. En el servicio EMR, seleccione su clúster y vaya a ‘Aplicaciones’.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/23.png)
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/24.png)
2. Seleccionar la URL del campo ‘Tonalidad’ e ingresar el usuario ‘hadoop’ y una contraseña de su gusto.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/34.png)

## Parte 7: Utilización de JupyterHub

Finalmente, para trabajar con JupyterHub:

1. En EMR, acceda a ‘Aplicaciones’ y elija JupyterHub.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/23.png)
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/24.png)
2. Ingrese con las credenciales usuario ‘jovyan’ y la contraseña ‘jupyter’ y cree un nuevo notebook de PySpark.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/35.png)
3. Verifique que las variables de contexto de Spark estén configuradas.
    ![Untitled](https://github.com/acarmonag/acarmonag-st0263/blob/master/Lab3/0/IMGS/36.png)

Con estos pasos, tendrá un clúster EMR listo para utilizar en los laboratorios del curso.
