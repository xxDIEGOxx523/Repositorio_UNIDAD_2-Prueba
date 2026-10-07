from abc import ABC, abstractmethod
from typing import List, Dict, Any

class IRegistroTiempoDAO(ABC):
    @abstractmethod
    def insertar(self, registro) -> bool: pass
    @abstractmethod
    def obtener_todos_con_detalles(self) -> List[Dict[str, Any]]: pass

class IEmpleadoDAO(ABC):
    @abstractmethod
    def obtener_todos(self) -> List[Dict[str, Any]]: pass

class IProyectoDAO(ABC):
    @abstractmethod
    def obtener_todos(self) -> List[Dict[str, Any]]: pass

class IDepartamentoDAO(ABC):
    @abstractmethod
    def obtener_todos(self) -> List[Dict[str, Any]]: pass