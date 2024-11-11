// gestiónTienda.js
const { Productos, Clientes, Pedidos, Informes } = require('./tiendaModules');

// Ejemplo de productos iniciales
Productos.agregarProducto({ id: 1, nombre: 'Laptop', precio: 1200, categoria: 'Electrónica', enStock: true });
Productos.agregarProducto({ id: 2, nombre: 'Auriculares', precio: 150, categoria: 'Electrónica', enStock: true });
Productos.agregarProducto({ id: 3, nombre: 'Camisa', precio: 40, categoria: 'Ropa', enStock: true });

// Ejemplo de clientes iniciales
Clientes.registrarCliente({ id: 1, nombre: 'Carlos', email: 'carlos@ejemplo.com' });
Clientes.registrarCliente({ id: 2, nombre: 'Ana', email: 'ana@ejemplo.com' });

// Crear pedidos
Pedidos.crearPedido({ clienteId: 1, productos: [1, 2] });
Pedidos.crearPedido({ clienteId: 2, productos: [3] });

// Generación de informes
console.log('Estadísticas de ventas:', Informes.generarEstadisticasVentas());
console.log('Productos más vendidos:', Informes.productosMasVendidos());
console.log('Clientes con mayor gasto:', Informes.clientesMayorGasto());
