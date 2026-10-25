"""Módulo principal que maneja la interfaz de usuario por consola."""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from Pronostico_Clima import obtener_datos_clima

# Reemplaza con tu API Key gratuita de OpenWeatherMap
API_KEY: str = "5cee196c513508d3ca93ad83e3fad172" 
console = Console()


def mostrar_clima(datos: dict) -> None:
    """Muestra los datos meteorológicos formateados en una tabla de Rich.

    Args:
        datos (dict): Datos retornados por la API de clima.
    """
    nombre_ciudad: str = datos.get("name", "Desconocida")
    pais: str = datos.get("sys", {}).get("country", "")
    temp: float = datos.get("main", {}).get("temp", 0.0)
    sensacion: float = datos.get("main", {}).get("feels_like", 0.0)
    humedad: int = datos.get("main", {}).get("humidity", 0)
    descripcion: str = datos.get("weather", [{}])[0].get("description", "").capitalize()

    tabla = Table(title=f"Clima en {nombre_ciudad}, {pais}", style="bold cyan")
    tabla.add_column("Métrica", style="bold white", justify="left")
    tabla.add_column("Valor", style="green", justify="right")

    tabla.add_row("Estado", descripcion)
    tabla.add_row("Temperatura", f"{temp} °C")
    tabla.add_row("Sensación Térmica", f"{sensacion} °C")
    tabla.add_row("Humedad", f"{humedad}%")

    console.print(tabla)


def main() -> None:
    """Función principal que ejecuta el bucle de la aplicación de consola."""
    console.print(Panel.fit("[bold blue]Bienvenido a la App de Clima[/bold blue]"))

    while True:
        try:
            ciudad: str = input("\nIngrese el nombre de la ciudad (o 'salir' para finalizar): ").strip()
            if not ciudad:
                console.print("[bold yellow]Por favor, ingrese un nombre válido.[/bold yellow]")
                continue
            if ciudad.lower() == "salir":
                console.print("[bold green]¡Gracias por usar la aplicación![/bold green]")
                break

            console.print("[dim]Consultando datos...[/dim]")
            datos: dict | None = obtener_datos_clima(ciudad, API_KEY)

            if datos:
                mostrar_clima(datos)
            else:
                console.print(f"[bold red]Error:[bold red] No se encontraron datos para '{ciudad}' o hay problemas de conexión.")

        except KeyboardInterrupt:
            console.print("\n[bold green]Programa interrumpido por el usuario. ¡Hasta luego![/bold green]")
            break
        except Exception as e:
            console.print(f"[bold red]Ocurrió un error inesperado: {e}[/bold red]")


if __name__ == "__main__":
    main()