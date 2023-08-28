from concurrent import futures
import grpc
import Service_pb2
import Service_pb2_grpc

# Dirección y puerto donde el servidor estará escuchando
HOST = '0.0.0.0:50051'

# Implementación del servicio ProductService
class ProductService(Service_pb2_grpc.ProductServiceServicer):
   
   # Implementación de la función SearchProduct
   def SearchProduct(self, request, context):
      print("Solicitud recibida para buscar producto: " + request.busqueda)
      # Aquí se puede agregar la lógica para buscar el producto
      return Service_pb2.singleTransactionResponse(nombre="nombre_del_archivo", last_updated="fecha", size=1.2)

   # Implementación de la función ListProducts
   def ListProducts(self, request, context):
      print("Solicitud recibida para listar productos")
      # Aquí se puede agregar la lógica para listar los productos
      # Por ahora, solo se devuelve un producto de ejemplo
      yield Service_pb2.Archive(busqueda="nombre_del_archivo_ejemplo")

def serve():
    # Crear el servidor gRPC
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Service_pb2_grpc.add_ProductServiceServicer_to_server(ProductService(), server)
    server.add_insecure_port(HOST)
    print("El servicio está corriendo en", HOST)
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
