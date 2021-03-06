from repositorios import Repositorios


class ProductoService():

    def get_productosList(self):
        return Repositorios.productosList

    def add_producto(self, producto):
        lastKey = -1
        for i in Repositorios.productosList:
            lastKey = i
        productokey = lastKey + 1
        Repositorios.productosList[productokey] = producto.__dict__
        return productokey

    def delete_producto(self, key):
        lastKey = -1
        for i in Repositorios.productosList:
            lastKey = i
        maxkey = lastKey
        if key > maxkey:
            raise ValueError("no se puede eliminar si el id no existe")
        del Repositorios.productosList[key]

    def insertion_sort_precio(self, listaDesordenada, tipo_orden):
        dic = listaDesordenada
        precio = {}
        for key in range(len(dic)):
            precio[key] = dic[key]['_precio']
            j = key
            precioActual = precio[key]
            dicActual = dic[key]
            if tipo_orden == "ascendente":
                while j > 0 and precio[j-1] > precioActual:
                    precio[j] = precio[j-1]
                    dic[j] = dic[j-1]
                    j = j - 1
                dic[j] = dicActual
                precio[j] = precioActual
            elif tipo_orden == "descendente":
                while j > 0 and precio[j-1] < precioActual:
                    precio[j] = precio[j-1]
                    dic[j] = dic[j-1]
                    j = j - 1
                dic[j] = dicActual
                precio[j] = precioActual
        return dic

    def busqueda_binaria(self, listaDesordenada, precio_buscado):
        dic = self.insertion_sort_precio(listaDesordenada, "ascendente")
        keyBuscada = len(dic)//2
        while dic[keyBuscada]["_precio"] != precio_buscado:
            keydezplazamiento = keyBuscada//2
            if keydezplazamiento == 0:
                keydezplazamiento = 1
            if dic[keyBuscada]["_precio"] < precio_buscado:
                keyBuscada = keyBuscada + keydezplazamiento
            elif dic[keyBuscada]["_precio"] > precio_buscado:
                keyBuscada = keyBuscada - keydezplazamiento
        return dic[keyBuscada]

    def update_producto(self, productoKey):
        lastKey = -1
        for i in Repositorios.productosList:
            lastKey = i
        maxkey = lastKey
        if productoKey > maxkey:
            raise ValueError("no se puede modificar si el legajo no existe")
        Repositorios.productosList[productoKey]['_estado'] = "vendido"

    def listarDisponibles(self):
        j = 0
        listado = {}
        for key in Repositorios.productosList:
            if Repositorios.productosList[key]['_estado'] == 'disponible':
                listado[j] = Repositorios.productosList[key]
                j = j + 1
        return listado
