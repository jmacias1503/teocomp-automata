def concatenar(afd1, afd2):
    nuevos_estados = afd1.estados + afd2.estados
    nuevo_alfabeto = afd1.alfabeto | afd2.alfabeto
    nuevo_inicial = afd1.estado_inicial
    nuevos_finales = afd2.estados_finales

    nuevas_transiciones = {}
    for estado in afd1.estados:
        nuevas_transiciones[estado] = {}
        for simbolo in afd1.alfabeto:
            nuevas_transiciones[estado][simbolo] = afd1.transiciones[estado][simbolo]
        if estado in afd1.estados_finales:
            nuevas_transiciones[estado]['ε'] = afd2.estado_inicial

    for estado in afd2.estados:
        nuevas_transiciones[estado] = {}
        for simbolo in afd2.alfabeto:
            nuevas_transiciones[estado][simbolo] = afd2.transiciones[estado][simbolo]

    afn_concatenado = AFN(
        estados = nuevos_estados,
        alfabeto = nuevo_alfabeto,
        transiciones = nuevas_transiciones,
        estado_inicial = nuevo_inicial,
        estados_finales = nuevos_finales
    )
