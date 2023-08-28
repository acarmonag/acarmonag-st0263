from flask import Flask, jsonify, request
import recursos_grpc

app = Flask(__name__)
recursos = recursos_grpc.RecursosGRPC()

@app.route('/buscar_producto', methods=['GET'])
def buscar_producto():
    nombre_archivo = request.args.get('nombre_archivo')
    respuesta = recursos.buscar_producto(nombre_archivo)
    return jsonify(respuesta)

@app.route('/listar_productos', methods=['GET'])
def listar_productos():
    archivos = recursos.listar_productos()
    return jsonify({"archivos": archivos})

if __name__ == "__main__":
    app.run(debug=True)
