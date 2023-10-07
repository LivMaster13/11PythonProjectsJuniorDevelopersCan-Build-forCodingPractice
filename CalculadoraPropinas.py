# Solicitar al usuario el monto de la factura y el porcentaje de propina
monto_factura = float(input("Ingrese el monto de la factura: $"))
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar (por ejemplo, 15 para el 15%): "))

# Calcular la propina
propina = (monto_factura * porcentaje_propina) / 100

# Calcular el total a pagar (factura + propina)
total_a_pagar = monto_factura + propina

# Mostrar el monto de la propina y el total a pagar
print(f"Propina a dejar: ${propina:.2f}")
print(f"Total a pagar: ${total_a_pagar:.2f}")


