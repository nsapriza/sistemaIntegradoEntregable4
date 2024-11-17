import main

class API:
    consulta = ""

    def cargar_consulta(self,param):
        self.consulta += param
        return self
    
    def traeme(self):
        self.consulta += f"SELECT "
        return self
    
    def de_la_tabla(self):
        self.consulta += f"FROM "
        return self
    
    def donde(self):
        self.consulta += f"WHERE "
        return self
    
    def agrupando_por(self):
        self.consulta += f"GROUP BY "
        return self
    
    def mezclando(self):
        self.consulta += f"JOIN "
        return self
    
    def en(self):
        self.consulta += f"ON "
        return self
    
    def los_distintos(self):
        self.consulta += f"DISTINCT "
        return self
    
    def contando(self):
        self.consulta += f"COUNT "
        return self
    
    def mete_en(self):
        self.consulta += f"INSERT INTO "
        return self
    
    def los_valores(self,param):
        self.consulta += f"VALUES "
        if type(param) != type([]):
            raise SyntaxError("valores deben ser un array")
        self.consulta += "("
        for i in param:
            self.consulta += str(i) + ","
        self.consulta = self.consulta[0:len(self.consulta)-1]
        self.consulta += ") "
        return self
    
    def actualiza(self):
        self.consulta += f"UPDATE "
        return self

    def setea(self):
        self.consulta += f"SET "
        return self
    
    def borra_de_la(self):
        self.consulta += f"DELETE FROM "
        return self
    
    def ordena_por(self):
        self.consulta += f"ORDER BY "
        return self

    def como_mucho(self):
        self.consulta += f"LIMIT "
        return self
    
    def mete_en(self):
        self.consulta += f"INSERT INTO "
        return self
    
    def where_del_group_by(self):
        self.consulta += f"HAVING "
        return self
    
    def en_esto(self):
        self.consulta += f"IN "
        return self
    
    def entre(self):
        self.consulta += f"BETWEEN "
        return self
    
    def parecido_a(self):
        self.consulta += f"LIKE "
        return self
    
    def y(self):
        self.consulta += f"AND "
        return self
    
    def cambia_la_tabla(self):
        self.consulta += f"ALTER TABLE "
        return self

    def agregar_columna(self):
        self.consulta += f"ADD COLUMN "
        return self
    
    def eliminar_columna(self):
        self.consulta += f"DROP COLUMN "
        return self
    
    def crea_la_tabla(self):
        self.consulta += f"CREATE TABLE "
        return self
    
    def por_defecto(self):
        self.consulta += f"DEFAULT "
        return self
    
    def unico(self):
        self.consulta += f"UNIQUE "
        return self
    
    def clave_prima(self):
        self.consulta += f"PRIMARY KEY "
        return self
    
    def clave_referente(self):
        self.consulta += f"FOREIGN KEY "
        return self

    def no_nulo(self):
        self.consulta += f"NOT NULL "
        return self
    
    def todo(self):
        self.consulta += f"* "
        return self
    
    def nombre(self,param:str):
        self.consulta += f"{param.lower()} "
        return self
    
    def numero(self,param):
        self.consulta += str(param)
        return self
    
    def operador(self,op):
        valid_operators = [">","<",">=","<=","=",".",",","*"]
        if op in valid_operators:
            self.consulta += f"{op} "
        else:
            raise TypeError("invalid operator")
        return self
    
    def columnas(self,param):
        if type(param) != type([]):
            raise SyntaxError("columnas deben ser un array")
        self.consulta += "("
        for i in param:
            self.consulta += i + ","
        self.consulta = self.consulta[0:len(self.consulta)-1]
        self.consulta += ") "
        return self
    
    def final_de_consulta(self):
        self.consulta += ";\n"
        return self
    
    def ejecutar(self):
        parser = main.parser
        self.consulta = self.consulta[0:len(self.consulta)-1]
        for i in self.consulta.split("\n"):
            parser.parse("".join(i.split(" ")))
        return self
    
    def limpiar_consulta(self):
        self.consulta = ""
        return self


if __name__ == "__main__":
    a = API()
    print("Traduciendo la sentencia: traeme todo de la tabla Profesores donde sueldo = 25; ")
    a.traeme().todo().de_la_tabla().nombre("Profesores").donde().nombre("sueldo").operador("=").numero(25).final_de_consulta()
    print(a.consulta)
    print("Traduciendo la sentencia: traeme todo de la tabla usuarios donde edad > 18; ")
    a = API()
    a.traeme().todo().de_la_tabla().nombre("usuarios").donde().nombre("edad").operador(">").numero(18).final_de_consulta()
    print(a.consulta)
    print("Traduciendo la sentencia: mete en usuarios (nombre) valor (25); ")
    a = API()
    a.mete_en().nombre("users").columnas(["nombre"]).los_valores([25]).final_de_consulta()
    print(a.consulta)