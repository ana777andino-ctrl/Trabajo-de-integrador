from dataclasses import dataclass


@dataclass
class vaca:
    id:int
    nombre: str
    raza: str
    cédula: str
    color: str
    peso: float
    departamento: str


@dataclass
class finca:
    nombres:str
    apellidos: str 
    cédula: str
    célular: int
    nombre_finca: str
    nombre_de_finca: str 
    ID_de_finca: int

@dataclass
class vendedor:
    nombre: str
    apellidos: str
    cédula: str 
    célular: int
    ID_de_finca: int
    ID_de_vaca: int
    peso : float
    antecedentes: str
    comprada : bool
    criollo :bool
    ubicación : str
    departamento: str
    precio_de_venta : float


@dataclass
class Remedio :
    nombre: str
    descripcion: str
    precio: float
    cantidad: int
    id_remedio: int | None = None

@dataclass
class comprador :
    nombre: str
    apellidos: str
    cédula: str
    célular: int
    departamento: str
    presupuesto: float

    