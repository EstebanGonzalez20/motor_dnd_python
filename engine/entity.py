from engine.component import Component

class Entity:
    """
    Esta clase representa a las entidades del juego.

    ATRIBUTOS:
        name: El nombre de la entidad

    METODOS:
        add: Añade un componente
        get: Obtiene un comoponente
        has: Consulta la existencia de un componente
    """
    def __init__(self, name: str):
        self.name = name
        self.components : dict[type, Component] = {}

    def add(self, component: Component) -> None:
        """
        Este método añade un componente al diccionario
        que contiene los comoponentes de la entidad.

        PARAMETROS:
            component: El componente que se agrega
        """
        self.components[type(component)] = component

    def get(self, component_type: type) -> Component | None:
        """
        Este método devuelve el componente asociado al
        tipo en el diccionario de componentes. En caso
        de no tener dicho tipo de componente devolvera
        None.

        PARAMETROS:
            comoponent_type: El tipo de componente que queremos obtener
        """
        return self.components.get(component_type)

    def has(self, component_type: type) -> bool:
        """
        Este método averigua si la entidad cuenta con
        el componente especificado, devolviendo true
        en caso de tenerlo y false en caso de que no.

        PARAMETROS:
            component_type: El tipo de componente que queremos consultar
        """
        return component_type in self.components