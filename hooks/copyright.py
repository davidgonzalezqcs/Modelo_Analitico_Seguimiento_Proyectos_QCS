from datetime import datetime

MESES = {
    1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
    5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
    9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
}

def on_config(config):
    hoy = datetime.now()
    fecha = f"{hoy.day} de {MESES[hoy.month]} de {hoy.year}"
    config.copyright = config.copyright.replace("{{ fecha }}", fecha)
    return config