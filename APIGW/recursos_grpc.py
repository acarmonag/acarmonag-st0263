import grpc
import Service_pb2
import Service_pb2_grpc

class RecursosGRPC:
    def __init__(self, host='[::]:50051'):
        # Crear un canal de comunicación con el servidor gRPC
        self.canal = grpc.insecure_channel(host)
        # Crear un cliente para el servicio ProductService
        self.cliente = Service_pb2_grpc.ProductServiceStub(self.canal)

    def buscar_producto(self, nombre_archivo):
        respuesta = self.cliente.SearchProduct(Service_pb2.Archive(busqueda=nombre_archivo))
        return {"nombre": respuesta.nombre, "last_updated": respuesta.last_updated, "size": respuesta.size}

    def listar_productos(self):
        archivos = []
        for archivo in self.cliente.ListProducts(Service_pb2.Empty()):
            archivos.append(archivo.busqueda)
        return archivos
