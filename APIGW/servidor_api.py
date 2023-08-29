from flask import Flask, jsonify, request
import recursos_grpc
from config import*
from producerQueue import RunAMQP

app = Flask(__name__)
recursos = recursos_grpc.RecursosGRPC()

@app.route('/buscar_producto', methods=['GET'])
def buscar_producto():
    try:
        nombre_archivo = request.args.get('nombre_archivo')
        respuesta = recursos.buscar_producto(nombre_archivo)
        return jsonify(respuesta)
    except:
        respuesta=RunAMQP(nombre_archivo, function="SearchProduct")
        return jsonify(respuesta)

@app.route('/listar_productos', methods=['GET'])
def listar_productos():
    try:
        archivos = recursos.listar_productos()
        return jsonify({"archivos": archivos})
    except:
        respuesta=RunAMQP("", function="ListProducts")
        return jsonify(respuesta)

if __name__ == "__main__":
    app.run(debug=True, host= HOST_APIGW, port = PORT_APIGW)
    
