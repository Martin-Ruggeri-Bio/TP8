import unittest
from producto import Producto
from parameterized import parameterized
from productoServices import ProductoService
from repositorios import Repositorios


class TestProducto(unittest.TestCase):

    def test_uso_property(self):
        producto = Producto()
        producto.descripcion = 'acer A515'
        producto.precio = 500000
        producto.tipo = 'computadoras'
        self.assertDictEqual(producto.__dict__, {'_descripcion': 'acer A515',
                                                 '_precio': 500000,
                                                 '_tipo': 'computadoras',
                                                 '_estado': 'disponible'})

    def test_constructor_con_valores_iniciales(self):
        producto = Producto("Lenovo 450", 300000, 'computadoras')
        self.assertDictEqual(producto.__dict__, {'_descripcion': 'Lenovo 450',
                                                 '_precio': 300000,
                                                 '_tipo': 'computadoras',
                                                 '_estado': 'disponible'})

    @parameterized.expand([
            ("lenovo t490", 6000000, 'computadoras'),
            ("samsung s10", 200000, 'celular'),
            ("samsung s20", 400000, 'celular'),
            ("acer", 6000500, 'computadoras'),
            ("HP", 6000000, 'computadoras'),
        ])
    # Agregar un producto
    def test_add_producto(self, descripcion, precio, tipo):
        producto = Producto(descripcion, precio, tipo)
        productoKey = ProductoService().add_producto(producto)
        self.assertDictEqual(Repositorios.productosList[productoKey],
                             producto. __dict__)

    @parameterized.expand([
        ("lenovo t490", -2000, 'computadoras'),
    ])
    def test_precioValidate(self, descripcion, precio, tipo):
        with self.assertRaises(ValueError):
            Producto(descripcion, precio, tipo)

    @parameterized.expand([
        ("ascendente", {0: {'_descripcion': 'samsung s10', '_precio': 200000,
                            '_tipo': 'celular', '_estado': 'disponible'},
                        1: {'_descripcion': 'samsung s20', '_precio': 400000,
                            '_tipo': 'celular', '_estado': 'disponible'},
                        2: {'_descripcion': 'lenovo t490', '_precio': 6000000,
                            '_tipo': 'computadoras', '_estado': 'disponible'},
                        3: {'_descripcion': 'HP', '_precio': 6000000,
                            '_tipo': 'computadoras', '_estado': 'disponible'},
                        4: {'_descripcion': 'acer', '_precio': 6000500,
                            '_tipo': 'computadoras', '_estado': 'disponible'}}
         ),
        ("descendente", {0: {'_descripcion': 'acer', '_precio': 6000500,
                             '_tipo': 'computadoras', '_estado': 'disponible'},
                         1: {'_descripcion': 'lenovo t490', '_precio': 6000000,
                             '_tipo': 'computadoras', '_estado': 'disponible'},
                         2: {'_descripcion': 'HP', '_precio': 6000000,
                             '_tipo': 'computadoras', '_estado': 'disponible'},
                         3: {'_descripcion': 'samsung s20', '_precio': 400000,
                             '_tipo': 'celular', '_estado': 'disponible'},
                         4: {'_descripcion': 'samsung s10', '_precio': 200000,
                             '_tipo': 'celular', '_estado': 'disponible'}}
         ),
    ])
    def test_insertion_sort_precio(self, tipo_orden, list_ordenada):
        lista_ordenada = ProductoService().\
         insertion_sort_precio(Repositorios.productosList, tipo_orden)
        self.assertDictEqual(lista_ordenada, list_ordenada)

    def test_delete_producto(self):
        producto = Producto("HP", 3000, "PC")
        productoKey = ProductoService().add_producto(producto)
        ProductoService().delete_producto(productoKey)
        self.assertEqual(Repositorios.productosList.get(productoKey), None)
        print(ProductoService().get_productosList())

    @parameterized.expand([
        ("lenovo t490", 6000000, 'computadoras')
    ])
    def test_delete_producto_value_error(self, descripcion, precio, tipo):
        long_list = len(Repositorios.productosList)
        with self.assertRaises(ValueError):
            ProductoService().delete_producto(long_list+1)

    @parameterized.expand([
        (200000, {'_descripcion': 'samsung s10', '_precio': 200000,
                  '_tipo': 'celular', '_estado': 'disponible'}),
        (400000, {'_descripcion': 'samsung s20', '_precio': 400000,
                  '_tipo': 'celular', '_estado': 'disponible'}),
        (6000500, {'_descripcion': 'acer', '_precio': 6000500,
                   '_tipo': 'computadoras', '_estado': 'disponible'}),
    ])
    # Busqueda binaria
    def test_busqueda_binaria(self, precio_buscado, producto):
        busqueda = ProductoService().\
            busqueda_binaria(Repositorios.productosList, precio_buscado)
        self.assertDictEqual(busqueda, producto)

    @parameterized.expand([(2,), (3,)])
    def test_update_producto(self, productoKey):
        # Creamos producto
        productoVendido = Producto(
            Repositorios.productosList[productoKey]['_descripcion'],
            Repositorios.productosList[productoKey]['_precio'],
            Repositorios.productosList[productoKey]['_tipo'],
            "vendido")
        ProductoService().update_producto(productoKey)
        self.assertDictEqual(Repositorios.productosList[productoKey],
                             productoVendido.__dict__)

    def test_listar_disponibles(self, key={0: 0, 1: 1, 2: 4}):
        listado = ProductoService().listarDisponibles()
        listado2 = {}
        j = 0
        for productoKey in Repositorios.productosList:
            if Repositorios.productosList[productoKey] != 2 and\
               Repositorios.productosList[productoKey] != 3:
                listado2[j] = Repositorios.productosList[productoKey]
            j = j + 1
        self.assertDictEqual(listado, listado2)


if __name__ == '__main__':
    unittest.main()
