# Modelo-Lotka-volterra
Este repositorio contiene la implementación del modelo Lotka-Volterra con ayuda del lenguaje de programación Python, mediante un sistema de ecuaciones diferenciales que describe la dinámica de un sistema depredador-presa.
El modelo Lotka-Volterra es representado por un sistema de Ecuaciones Diferenciales Ordinarias que describe la interacción entre dos especies: presa y depredador. Su forma básica es:

 \[
\frac{dx}{dt} = \alpha x - \beta xy
\]

\[
\frac{dy}{dt} = \delta xy - \gamma y
\]

Donde:
- \( x \) representa la población de presas.
- \( y \) representa la población de depredadores.
- \( \alpha \) es la tasa de crecimiento de las presas en ausencia de depredadores.
- \( \beta \) es la tasa de depredación (eficiencia con la que los depredadores cazan presas).
- \( \delta \) es la eficiencia con la que los depredadores convierten presas en nuevos depredadores.
- \( \gamma \) es la tasa de mortalidad de los depredadores en ausencia de presas.
