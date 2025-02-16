# Modelo-Lotka-volterra
Este repositorio contiene la implementación del modelo Lotka-Volterra con ayuda del lenguaje de programación Python, mediante un sistema de ecuaciones diferenciales que describe la dinámica de un sistema depredador-presa.

El modelo Lotka-Volterra es un sistema de ecuaciones diferenciales que describe la interacción entre dos especies: una presa y un depredador. Su forma básica es:

𝑑
𝑥
𝑑
𝑡
=
𝛼
𝑥
−
𝛽
𝑥
𝑦
dt
dx
​
 =αx−βxy
𝑑
𝑦
𝑑
𝑡
=
𝛿
𝑥
𝑦
−
𝛾
𝑦
dt
dy
​
 =δxy−γy
donde:

𝑥
x es la población de presas.
𝑦
y es la población de depredadores.
𝛼
α es la tasa de crecimiento de la presa en ausencia de depredadores.
𝛽
β es la tasa de depredación (tasa a la que los depredadores cazan presas).
𝛿
δ es la eficiencia con la que los depredadores convierten presas en nuevos depredadores.
𝛾
γ es la tasa de mortalidad de los depredadores en ausencia de presas.
El siguiente código implementa este modelo utilizando la función solve_ivp de scipy.integrate para resolver las ecuaciones diferenciales.
