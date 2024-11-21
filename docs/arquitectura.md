# Arquitectura del Sistema

Este documento describe la arquitectura del sistema basado en Raft.

## Componentes

1. **Cliente**:
   Genera solicitudes y recibe respuestas.
2. **ProxyAplicación**:
   Redirige solicitudes al líder del clúster.
3. **NodoRaft**:
   Coordina las operaciones y replica logs.
4. **EntradaLog**:
   Representa las entradas replicadas.
