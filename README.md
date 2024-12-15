# Capstone // LlegOk

## Descripción del Proyecto
Capstone es un servicio web orientado a automatizar y optimizar el proceso de notificación y registro de encomiendas en edificios residenciales. Este sistema utiliza tecnologías avanzadas para:

1. Identificar al propietario de un paquete mediante el análisis de una etiqueta.
2. Notificar automáticamente al residente vía WhatsApp con:
   - Una imagen del paquete.
   - Un código QR que será utilizado por el conserje para verificar la identidad del residente.
3. Registrar automáticamente la llegada del paquete y su estado.
4. Permitir al conserje analizar el QR para marcar el paquete como entregado en los registros, evitando errores humanos.

### Objetivo
El objetivo principal de este proyecto es automatizar el proceso de notificación y registro de encomiendas, así como evitar errores humanos mediante la verificación automática y confiable de la identidad de los residentes.

## Integrantes del Equipo
- José Riquelme
- Valentina Albar
- José Sandoval

## Repositorios del Proyecto
El proyecto está dividido en varios microservicios, cada uno diseñado para una tarea específica, junto con el frontend:

### Microservicios
- **Microservicio Procesamiento de Imágenes**  
  [https://github.com/jiriquelme/ms-image-processing-service](https://github.com/jiriquelme/ms-image-processing-service)

- **Microservicio Análisis de Texto**  
  [https://github.com/jiriquelme/ms-text-analysis-service](https://github.com/jiriquelme/ms-text-analysis-service)

- **Microservicio de Servicio de Gestión**  
  [https://github.com/jiriquelme/ms-management-service](https://github.com/jiriquelme/ms-management-service)

- **Microservicio Servicio de Notificación**  
  [https://github.com/jiriquelme/ms-notification-service](https://github.com/jiriquelme/ms-notification-service)

### Frontend
- **Frontend**  
  [https://github.com/jiriquelme/LlegoOK](https://github.com/jiriquelme/LlegoOK)

## Características Principales
- **Identificación Automática:** Utiliza tecnologías como Google Vision AI para analizar etiquetas en los paquetes.
- **Notificaciones Instantáneas:** Enviadas vía WhatsApp con la información esencial.
- **Verificación de Identidad:** Uso de códigos QR para garantizar que el paquete sea entregado al destinatario correcto.
- **Registro Automatizado:** Mantiene un historial de paquetes recibidos y entregados.

## Tecnologías Utilizadas
- **Backend:** Django
- **Frontend:** React Native
- **Microservicios:** División funcional en diferentes servicios desplegados en contenedores Docker.
- **Notificaciones:** Twilio API para mensajes de WhatsApp.
- **Análisis de Texto:** OpenAI GPT para contextualizar información de etiquetas.
- **Procesamiento de Imágenes:** Google Vision AI para la detección de texto en etiquetas.
- **Almacenamiento:** Google Cloud Storage para gestionar las imágenes de etiquetas y QR.

## Estructura del Sistema
1. **Microservicio Procesamiento de Imágenes:** Analiza la etiqueta de un paquete para extraer información textual.
2. **Microservicio Análisis de Texto:** Interpreta el texto detectado para identificar el código del departamento.
3. **Microservicio de Servicio de Gestión:** Maneja los datos de residentes, departamentos y encomiendas.
4. **Microservicio Servicio de Notificación:** Envía notificaciones vía WhatsApp con detalles del paquete.
5. **Frontend:** Interfaz móvil intuitiva para conserjes y administradores de edificios.

---
Este proyecto representa un paso adelante en la gestión automatizada de encomiendas, garantizando eficiencia, precisión y una experiencia fluida para los residentes y conserjes.
