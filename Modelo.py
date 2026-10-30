def calcular_equilibrio():

	s = float(input("Precio de venta por unidad: (s) "))
	f = float(input("Costo fijo: (f) "))
	v = float(input("Costo variable por unidad: (v) "))
	x = float(input("Numero de unidades vendidas (x) "))

	if s <= v:
		print("\n[Eror]: El precio de venta debe ser mayor que el costo variable")
		return 
	
	ganancia = (s - v) * x -f
	punto_de_equilibrio = f / (s - v)

	print(f"Ganancia Total: ${ganancia:,.2f}")
	print(f"Punto de Equilibrio: {punto_de_equilibrio:,.2f} unidades")
if __name__ == "__main__":
	calcular_equilibrio()
