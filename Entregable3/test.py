import unittest
from API import API

class TestAPI(unittest.TestCase):
    
    def setUp(self):
        # This method will run before every test
        self.api = API()
    
    def test_cargar_consulta(self):
        result = self.api.cargar_consulta("SELECT * FROM users")
        self.assertEqual(result.consulta, "SELECT * FROM users")

    def test_traeme(self):
        result = self.api.traeme()
        self.assertEqual(result.consulta, "SELECT ")

    def test_de_la_tabla(self):
        result = self.api.de_la_tabla()
        self.assertEqual(result.consulta, "FROM ")

    def test_donde(self):
        result = self.api.donde()
        self.assertEqual(result.consulta, "WHERE ")

    def test_agrupando_por(self):
        result = self.api.agrupando_por()
        self.assertEqual(result.consulta, "GROUP BY ")

    def test_mezclando(self):
        result = self.api.mezclando()
        self.assertEqual(result.consulta, "JOIN ")

    def test_en(self):
        result = self.api.en()
        self.assertEqual(result.consulta, "ON ")

    def test_los_distintos(self):
        result = self.api.los_distintos()
        self.assertEqual(result.consulta, "DISTINCT ")

    def test_contando(self):
        result = self.api.contando()
        self.assertEqual(result.consulta, "COUNT ")

    def test_mete_en(self):
        result = self.api.mete_en()
        self.assertEqual(result.consulta, "INSERT INTO ")

    def test_los_valores(self):
        result = self.api.los_valores([""])
        self.assertEqual(result.consulta, "VALUES () ")

    def test_actualiza(self):
        result = self.api.actualiza()
        self.assertEqual(result.consulta, "UPDATE ")

    def test_setea(self):
        result = self.api.setea()
        self.assertEqual(result.consulta, "SET ")

    def test_borra_de_la(self):
        result = self.api.borra_de_la()
        self.assertEqual(result.consulta, "DELETE FROM ")

    def test_ordena_por(self):
        result = self.api.ordena_por()
        self.assertEqual(result.consulta, "ORDER BY ")

    def test_como_mucho(self):
        result = self.api.como_mucho()
        self.assertEqual(result.consulta, "LIMIT ")

    def test_where_del_group_by(self):
        result = self.api.where_del_group_by()
        self.assertEqual(result.consulta, "HAVING ")

    def test_en_esto(self):
        result = self.api.en_esto()
        self.assertEqual(result.consulta, "IN ")

    def test_entre(self):
        result = self.api.entre()
        self.assertEqual(result.consulta, "BETWEEN ")

    def test_parecido_a(self):
        result = self.api.parecido_a()
        self.assertEqual(result.consulta, "LIKE ")

    def test_y(self):
        result = self.api.y()
        self.assertEqual(result.consulta, "AND ")

    def test_cambia_la_tabla(self):
        result = self.api.cambia_la_tabla()
        self.assertEqual(result.consulta, "ALTER TABLE ")

    def test_agregar_columna(self):
        result = self.api.agregar_columna()
        self.assertEqual(result.consulta, "ADD COLUMN ")

    def test_eliminar_columna(self):
        result = self.api.eliminar_columna()
        self.assertEqual(result.consulta, "DROP COLUMN ")

    def test_crea_la_tabla(self):
        result = self.api.crea_la_tabla()
        self.assertEqual(result.consulta, "CREATE TABLE ")

    def test_por_defecto(self):
        result = self.api.por_defecto()
        self.assertEqual(result.consulta, "DEFAULT ")

    def test_unico(self):
        result = self.api.unico()
        self.assertEqual(result.consulta, "UNIQUE ")

    def test_clave_prima(self):
        result = self.api.clave_prima()
        self.assertEqual(result.consulta, "PRIMARY KEY ")

    def test_clave_referente(self):
        result = self.api.clave_referente()
        self.assertEqual(result.consulta, "FOREIGN KEY ")

    def test_no_nulo(self):
        result = self.api.no_nulo()
        self.assertEqual(result.consulta, "NOT NULL ")

    def test_todo(self):
        result = self.api.todo()
        self.assertEqual(result.consulta, "* ")

    def test_nombre(self):
        result = self.api.nombre("Tabla")
        self.assertEqual(result.consulta, "tabla ")

    def test_numero(self):
        result = self.api.numero(10)
        self.assertEqual(result.consulta, "10")

    def test_operador(self):
        result = self.api.operador("=")
        self.assertEqual(result.consulta, "= ")

    def test_operador_invalid(self):
        with self.assertRaises(TypeError):
            self.api.operador("invalid")

    def test_final_de_consulta(self):
        result = self.api.final_de_consulta()
        self.assertEqual(result.consulta, ";\n")
    
    def test_select_statement_valid(self):
        # Construct a valid SELECT statement
        result = (self.api
                  .traeme()
                  .todo()
                  .de_la_tabla()
                  .nombre("users")
                  .donde()
                  .nombre("age")
                  .operador(">")
                  .numero(21)
                  .final_de_consulta()
                  .ejecutar().limpiar_consulta())
        self.assertIsInstance(result, API)
    
    def test_insert_statement_valid(self):
        # Construct a valid INSERT statement
        result = (self.api
                  .mete_en()
                  .nombre("users")
                  .columnas(["nombre"])
                  .los_valores([25])
                  .final_de_consulta()
                  .ejecutar().limpiar_consulta())
        self.assertIsInstance(result, API)

    def test_update_statement_valid(self):
        # Construct a valid UPDATE statement
        result = (self.api
                  .actualiza()
                  .nombre("users")
                  .setea()
                  .nombre("age")
                  .operador("=")
                  .numero(30)
                  .donde()
                  .nombre("id")
                  .operador("=")
                  .numero(1)
                  .final_de_consulta()
                  .ejecutar().limpiar_consulta())
        self.assertIsInstance(result, API)

    def test_delete_statement_valid(self):
        # Construct a valid DELETE statement
        result = (self.api
                  .borra_de_la()
                  .nombre("users")
                  .donde()
                  .nombre("age")
                  .operador("<")
                  .numero(18)
                  .final_de_consulta()
                  .ejecutar().limpiar_consulta())
        self.assertIsInstance(result, API)

    def test_invalid_syntax_error(self):
        # Construct an invalid statement to raise SyntaxError
        with self.assertRaises(SyntaxError):
            (self.api
             .traeme()
             .todo()
             .donde()  # Missing 'FROM table'
             .nombre("age")
             .operador(">")
             .numero(21)
             .final_de_consulta()
             .ejecutar().limpiar_consulta())
    
    def test_select_with_group_by_valid(self):
        # Construct a valid SELECT with GROUP BY
        result = (self.api
                  .traeme()
                  .todo()
                  .de_la_tabla()
                  .nombre("orders")
                  .agrupando_por()
                  .nombre("customer_id")
                  .final_de_consulta()
                  .ejecutar().limpiar_consulta())
        self.assertIsInstance(result, API)
    
    def test_select_with_order_by_valid(self):
        # Construct a valid SELECT with ORDER BY
        result = (self.api
                  .traeme()
                  .todo()
                  .de_la_tabla()
                  .nombre("products")
                  .ordena_por()
                  .nombre("price")
                  .final_de_consulta()
                  .ejecutar().limpiar_consulta())
        self.assertIsInstance(result, API)

    def test_invalid_operator_raises_error(self):
        # Using an invalid operator should raise a TypeError
        with self.assertRaises(TypeError):
            (self.api
             .traeme()
             .todo()
             .de_la_tabla()
             .nombre("users")
             .donde()
             .nombre("age")
             .operador("invalid")  # Invalid operator
             .numero(21)
             .final_de_consulta()
             .ejecutar().limpiar_consulta())

if __name__ == '__main__':
    unittest.main()

