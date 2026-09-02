# Ana añade esta función a src/pipeline.py (al final, antes del if __name__)

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
