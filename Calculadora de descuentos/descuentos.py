# Calculadora de descuentos simple

def descuentos(precio, descuento):

    unitario = descuento/100
    
    return f"El precio del productos es de {precio} \nCon el {descuento}% de descuento el valor es de {precio*(1-unitario)} \nEl ahorro es de {precio*unitario}"