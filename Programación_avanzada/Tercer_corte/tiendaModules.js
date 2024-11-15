// Almacenamiento
const productos = []; // Array que almacena los productos
const clientes = []; // Array que almacena los clientes
const pedidos = []; // Array que almacena los pedidos

// Módulo de Productos
const Productos = {
    // Función para agregar un producto al inventario
    agregarProducto: (producto) => {
        productos.push(producto); // Se agrega el producto al array de productos
        console.log(`Producto agregado: ${producto.nombre}`); // Mensaje de confirmación
    },

    // Función para actualizar un producto basado en su ID
    actualizarProducto: (id, actualizacion) => {
        const producto = productos.find((p) => p.id === id); // Buscar producto por ID
        if (producto) Object.assign(producto, actualizacion); // Si se encuentra, se actualiza el producto
        console.log(
            `Producto actualizado: ${producto ? producto.nombre : "No encontrado"}`
        ); // Mensaje de confirmación
    },

    // Función para eliminar un producto basado en su ID
    eliminarProducto: (id) => {
        const index = productos.findIndex((p) => p.id === id); // Buscar el índice del producto por ID
        if (index !== -1) productos.splice(index, 1); // Si se encuentra, se elimina del array
        console.log(`Producto eliminado: ID ${id}`); // Mensaje de confirmación
    },

    // Función para obtener un producto por su ID
    obtenerProducto: (id) => productos.find((p) => p.id === id), // Buscar y retornar el producto por ID

    // Función para listar todos los productos
    listarProductos: () => productos, // Retorna el array de productos
};

// Módulo de Clientes
const Clientes = {
    // Función para registrar un cliente en el sistema
    registrarCliente: (cliente) => {
        clientes.push(cliente); // Se agrega el cliente al array de clientes
        console.log(`Cliente registrado: ${cliente.nombre}`); // Mensaje de confirmación
    },

    // Función para actualizar los datos de un cliente basado en su ID
    actualizarCliente: (id, actualizacion) => {
        const cliente = clientes.find((c) => c.id === id); // Buscar cliente por ID
        if (cliente) Object.assign(cliente, actualizacion); // Si se encuentra, se actualiza el cliente
        console.log(
            `Cliente actualizado: ${cliente ? cliente.nombre : "No encontrado"}`
        ); // Mensaje de confirmación
    },

    // Función para obtener un cliente por su ID
    obtenerCliente: (id) => clientes.find((c) => c.id === id), // Buscar y retornar el cliente por ID

    // Función para listar todos los clientes
    listarClientes: () => clientes, // Retorna el array de clientes
};

// Módulo de Pedidos
const Pedidos = {
    // Función para crear un pedido para un cliente
    crearPedido: ({ clienteId, productos: productosIds }) => {
        const cliente = Clientes.obtenerCliente(clienteId); // Obtener el cliente por su ID
        if (!cliente) return console.log(`Cliente no encontrado: ID ${clienteId}`); // Si el cliente no se encuentra, se muestra un mensaje

        // Buscar productos asociados al pedido mediante sus IDs
        const productosPedido = productosIds
            .map((id) => Productos.obtenerProducto(id))
            .filter(Boolean);

        // Calcular el total del pedido
        const total = productosPedido.reduce((sum, prod) => sum + prod.precio, 0);

        // Crear el pedido con la información obtenida
        const pedido = {
            id: pedidos.length + 1,
            clienteId,
            productos: productosPedido,
            total,
        };
        pedidos.push(pedido); // Agregar el pedido al array de pedidos
        console.log(`Pedido creado para ${cliente.nombre}, Total: $${total}`); // Mensaje de confirmación
    },

    // Función para listar todos los pedidos
    listarPedidos: () => pedidos, // Retorna el array de pedidos
};

// Módulo de Informes
const Informes = {
    // Función para generar estadísticas de ventas
    generarEstadisticasVentas: () => {
        const totalVentas = pedidos.reduce(
            (total, pedido) => total + pedido.total,
            0
        ); // Sumar todos los totales de los pedidos
        const totalPedidos = pedidos.length; // Contar la cantidad de pedidos
        const promedioVenta = totalVentas / totalPedidos || 0; // Calcular el promedio de ventas

        // Retornar las estadísticas generadas
        return { totalVentas, totalPedidos, promedioVenta };
    },

    // Función para obtener los productos más vendidos
    productosMasVendidos: () => {
        const contadorProductos = productos.reduce((contadores, prod) => {
            contadores[prod.nombre] = 0; // Inicializar contador de productos
            return contadores;
        }, {});

        // Contar la cantidad de veces que cada producto aparece en los pedidos
        pedidos.forEach((pedido) => {
            pedido.productos.forEach((prod) => {
                contadorProductos[prod.nombre] =
                    (contadorProductos[prod.nombre] || 0) + 1;
            });
        });

        // Ordenar los productos más vendidos y retornarlos
        return Object.entries(contadorProductos).sort((a, b) => b[1] - a[1]);
    },

    // Función para obtener los clientes con mayor gasto
    clientesMayorGasto: () => {
        const gastosClientes = clientes.map((cliente) => {
            const totalGastado = pedidos
                .filter((pedido) => pedido.clienteId === cliente.id) // Filtrar los pedidos del cliente
                .reduce((total, pedido) => total + pedido.total, 0); // Calcular el gasto total del cliente

            return { nombre: cliente.nombre, totalGastado }; // Retornar el cliente y su gasto total
        });

        // Ordenar los clientes por su gasto y retornarlos
        return gastosClientes.sort((a, b) => b.totalGastado - a.totalGastado);
    },
};

// Exportar los módulos para ser utilizados en otros archivos
module.exports = { Productos, Clientes, Pedidos, Informes };
