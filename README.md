# APIs Genericas de Bases de Datos

Iniciar el daemon de Docker

```bash
sudo systemctl start docker
```


Instalar las BDs (solo la primera vez)

> MySQL suele tardar un rato en encenderse

```bash
sudo ./scripts/install.sh
```

Iniciar/Parar ambas BDs a la vez

```bash
sudo ./scripts/start.sh
sudo ./scripts/stop.sh
```
