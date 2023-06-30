from uuid import uuid4
from operacion.Operacion import Operacion
from config.db import Conexion


class OperacionDAO:
    _SELECCIONAR = 'SELECT * FROM operacion'
    _INSERTAR = 'INSERT INTO operacion(id_operacion, tipo_operacion, cuerpo_operacion, resultado)VALUES (%s, %s, %s, %s)'

    @classmethod
    def obtenerDatos(cls):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                operaciones = []
                for registro in registros:
                    operacion = Operacion(
                        registro[1], registro[2], registro[3])
                    operaciones.append(operacion)
                Conexion._conexion = None
                Conexion._cursor = None
                return operaciones

    @classmethod
    def agregarDato(cls, operacion):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (uuid4(), operacion.tipoOperacion,
                           operacion.cuerpoOperacion, operacion.resultado)
                cursor.execute(cls._INSERTAR, valores)
                Conexion._conexion = None
                Conexion._cursor = None
                return cursor.rowcount
