# Inicio

## Contexto

**QCS es una empresa de consultoría** que ejecuta proyectos para clientes en múltiples sectores en *Colombia y Latinoamérica*, entre ellos cajas de compensación, salud, telecomunicaciones, gas, energía, turismo, comercio, minería, tecnología, gobierno, educación, finanzas y agricultura. A estos compromisos se les denomina internamente **Proyectos QCS**.

Para operar con eficiencia, **QCS necesita hacer seguimiento continuo a cada proyecto**: comparar lo que se planeó con lo que realmente se ejecutó, y con esa información tomar decisiones sobre el uso de sus recursos humanos, es decir, las horas trabajadas tanto por consultores internos como por apoyos externos.

El presente modelo nace de esa necesidad. Su propósito es **integrar las fuentes de información** relevantes **para** centralizar, parametrizar y automatizar ese **seguimiento**, tomando como fuente principal **Zoho Projects**, la herramienta corporativa de gestión de proyectos de QCS.


## Objetivo

Este documento presenta la documentación técnica del **Modelo Analítico de Seguimiento de Proyectos QCS**. Su propósito es explicar cómo configurar las herramientas involucradas, cómo se procesan los datos, qué medidas se calculan y cómo se visualizan en los tableros de control.

El modelo está diseñado bajo un principio de **automatización máxima**: toda la información se extrae directamente desde **Zoho Projects** sin intervención manual, lo que garantiza consistencia y calidad de los datos. Las únicas excepciones son **una tabla de homologación y una paramétrica de glosario**, que deben configurarse manualmente para los roles y el glosario.

## Alcance

Este modelo analítico está compuesto por múltiples elementos técnicos que deben considerarse en conjunto al momento de realizar cualquier modificación. **Un cambio en uno de ellos puede tener efectos en cascada sobre los demás**.

**Componentes del sistema:**

El modelo incluye **cuatro scripts de Python** para automatización (dos transversales de uso interno en QCS y dos específicos del modelo), **cuatro archivos de configuración en formato JSON** que contienen clientes, credenciales y tokens, **seis archivos Excel que funcionan como paramétricas**, **ocho archivos Excel de almacenamiento anualizado** de registros históricos de Zoho, **quince archivos Excel de salida** que alimentan el tablero de Power BI y finalmente **el tablero mismo construido en Power BI**.

**Información histórica y estructura de datos:**

El modelo cuenta con registros históricos de Zoho Projects **desde 2018**. Sin embargo, la estructura jerárquica actual (**Proyecto, Épica, Historia, Tarea**) junto con la asignación de horas planeadas por roles **fue adoptada apenas en 2025**. Para que los datos históricos sean compatibles con esta estructura, es necesario **ajustar manualmente las horas planeadas por roles directamente en Zoho Projects**.

**Proceso de actualización:**

El modelo se actualiza automáticamente **todos los días laborales** mediante dos scripts programados: el primero descarga la información nueva desde Zoho **a las 8:15 am**, y el segundo la procesa **a las 8:20 am**. Estos scripts se ejecutan **de forma local** en uno de los equipos del área de analítica de QCS. Una vez terminado el procesamiento automático, el tablero de Power BI queda listo para ser actualizado manualmente **a partir de las 8:30 am**.

## Mejoras a futuro

Las siguientes mejoras permitirían llevar el modelo a un nivel superior de automatización y escalabilidad, eliminando las intervenciones manuales que aún persisten:

Primero, **migrar el almacenamiento desde Google Drive hacia una base de datos SQL** alojada en un servidor dedicado. Esto mejoraría la velocidad de consulta, la integridad referencial de los datos y la capacidad de manejar volúmenes más grandes de información sin degradación de rendimiento.

Segundo, **trasladar la ejecución de los scripts Python desde equipos locales hacia un servidor o máquina virtual en la nube**. Esto eliminaría la dependencia de que un equipo físico específico esté encendido y disponible cada mañana, y permitiría implementar mecanismos de monitoreo, logs centralizados y recuperación ante fallos de forma más sencilla.

Tercero, **adquirir una licencia Premium de Power BI** que habilite la actualización automática de los tableros sin intervención humana. Esto cerraría el ciclo completo de automatización, desde la extracción de datos en Zoho hasta la visualización final disponible para los usuarios.

Estas tres mejoras tienen **costos asociados**, tanto de licenciamiento como de infraestructura, que deben evaluarse y mantenerse a lo largo del tiempo. La arquitectura actual del modelo fue diseñada para maximizar la automatización dentro de las restricciones presupuestarias existentes, aprovechando al máximo la licencia de Zoho Projects y el acceso corporativo a Google Drive.