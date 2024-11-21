# Proyecto Raft - ST0263

Este proyecto implementa el algoritmo de consenso **Raft** en un sistema distribuido simulado. Incluye mecanismos para manejar la elección de líder, replicación de logs y recuperación tras fallos, garantizando consistencia y disponibilidad.

---

## **Características Principales**
1. **Elección de Líder**:
   - Los nodos seguidores detectan la caída del líder y realizan una nueva elección automáticamente.
2. **Replicación de Logs**:
   - El líder coordina la replicación de datos a los seguidores.
3. **Simulación de Fallos**:
   - Simula la caída de nodos (líder o seguidores) y su posterior recuperación.
4. **Separación de Planos**:
   - **Plano de Datos**: Comunicación entre cliente y nodos para manejar solicitudes de lectura/escritura.
   - **Plano de Control**: Coordinación entre nodos para elecciones y replicación de logs.

---

## **Estructura del Proyecto**
.
├── README.md
├── docs
│   ├── algoritmo.md
│   └── arquitectura.md
├── requirements.txt
├── src
│   ├── cliente.py
│   ├── entrada_log.py
│   ├── main.py
│   ├── nodo_raft.py
│   ├── proxy.py
│   └── utils
└── tests
    ├── test_cliente.py
    ├── test_proxy.py
    └── test_raft.py

5 directories, 12 files

## **Requisitos**
- **Python 3.8+**
- Las dependencias se encuentran en `requirements.txt`.
**pip install -r requirements.txt**
