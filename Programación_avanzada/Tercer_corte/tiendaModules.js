// Almacenamiento inicial
const productos = [];
const clientes = [];
const pedidos = [];

// Módulo de Productos
const Productos = {
    agregarProducto: (producto) => {
        productos.push(producto);
        console.log(`Producto agregado: ${producto.nombre}`);
    },
    actualizarProducto: (id, actualizacion) => {
        const producto = productos.find(p => p.id === id);
        if (producto) Object.assign(producto, actualizacion);
        console.log(`Producto actualizado: ${producto ? producto.nombre : 'No encontrado'}`);
    },
    eliminarProducto: (id) => {
        const index = productos.findIndex(p => p.id === id);
        if (index !== -1) productos.splice(index, 1);
        console.log(`Producto eliminado: ID ${id}`);
    },
    obtenerProducto: (id) => productos.find(p => p.id === id),
    listarProductos: () => productos
};

// Módulo de Clientes
const Clientes = {
    registrarCliente: (cliente) => {
        clientes.push(cliente);
        console.log(`Cliente registrado: ${cliente.nombre}`);
    },
    actualizarCliente: (id, actualizacion) => {
        const cliente = clientes.find(c => c.id === id);
        if (cliente) Object.assign(cliente, actualizacion);
        console.log(`Cliente actualizado: ${cliente ? cliente.nombre : 'No encontrado'}`);
    },
    obtenerCliente: (id) => clientes.find(c => c.id === id),
    listarClientes: () => clientes
};

// Módulo de Pedidos
const Pedidos = {
    crearPedido: ({ clienteId, productos: productosIds }) => {
        const cliente = Clientes.obtenerCliente(clienteId);
        if (!cliente) return console.log(`Cliente no encontrado: ID ${clienteId}`);

        const productosPedido = productosIds.map(id => Productos.obtenerProducto(id)).filter(Boolean);
        const total = productosPedido.reduce((sum, prod) => sum + prod.precio, 0);

        const pedido = { id: pedidos.length + 1, clienteId, productos: productosPedido, total };
        pedidos.push(pedido);
        console.log(`Pedido creado para ${cliente.nombre}, Total: $${total}`);
    },
    listarPedidos: () => pedidos,
};

// Módulo de Informes
const Informes = {
    generarEstadisticasVentas: () => {
        const totalVentas = pedidos.reduce((total, pedido) => total + pedido.total, 0);
        const totalPedidos = pedidos.length;
        const promedioVenta = totalVentas / totalPedidos || 0;

        return { totalVentas, totalPedidos, promedioVenta };
    },
    productosMasVendidos: () => {
        const contadorProductos = productos.reduce((contadores, prod) => {
            contadores[prod.nombre] = 0;
            return contadores;
        }, {});

        pedidos.forEach(pedido => {
            pedido.productos.forEach(prod => {
                contadorProductos[prod.nombre] = (contadorProductos[prod.nombre] || 0) + 1;
            });
        });

        return Object.entries(contadorProductos).sort((a, b) => b[1] - a[1]);
    },
    clientesMayorGasto: () => {
        const gastosClientes = clientes.map(cliente => {
            const totalGastado = pedidos
                .filter(pedido => pedido.clienteId === cliente.id)
                .reduce((total, pedido) => total + pedido.total, 0);

            return { nombre: cliente.nombre, totalGastado };
        });

        return gastosClientes.sort((a, b) => b.totalGastado - a.totalGastado);
    }
};

// Exportar los módulos
module.exports = { Productos, Clientes, Pedidos, Informes };
