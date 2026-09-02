# src/pipeline.py - Pipeline de ventas de FreshData Corp

def cargar_ventas(archivo):
    """Carga datos de ventas desde un archivo CSV."""
    print(f"Cargando ventas desde: {archivo}")
    # Simulamos datos
    ventas = [
        {"tienda": "T001", "producto": "Leche", "cantidad": 150, "precio": 1.20},
        {"tienda": "T001", "producto": "Pan", "cantidad": 200, "precio": 0.80},
        {"tienda": "T002", "producto": "Leche", "cantidad": 90, "precio": 1.20},
        {"tienda": "T002", "producto": "Huevos", "cantidad": 75, "precio": 2.50},
    ]
    return ventas

def calcular_total_tienda(ventas, tienda_id, con_iva=True):
    """Calcula el total de ventas de una tienda (con IVA por defecto)."""
    total = 0
    for venta in ventas:
        if venta["tienda"] == tienda_id:
            total += venta["cantidad"] * venta["precio"]
    if con_iva:
        from config import IVA
        total *= (1 + IVA)
    return total

def resumen_por_producto(ventas):
    """Genera resumen de ventas agrupado por producto."""
    resumen = {}
    for venta in ventas:
        producto = venta["producto"]
        ingreso = venta["cantidad"] * venta["precio"]
        if producto in resumen:
            resumen[producto] += ingreso
        else:
            resumen[producto] = ingreso
    return resumen

if __name__ == "__main__":
    ventas = cargar_ventas("ventas_2024_01.csv")
    total = calcular_total_tienda(ventas, "T001")
    print(f"Total tienda T001: ${total:.2f}")
