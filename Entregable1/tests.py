import unittest
from unittest import mock
from main import *

class TestFunctions(unittest.TestCase):
    data:list[list] = imp_csv()

    def test_get_pregunta(self):
        temp_data:list = self.data[0:2]
        self.assertEqual(get_pregunta(temp_data)["category"],temp_data[1][0])
        self.assertEqual(get_pregunta(temp_data)["answer"],temp_data[1][3])
        self.assertEqual(get_pregunta(temp_data)["question"],temp_data[1][2])
    
    def test_filter_by_category(self):
        pregunta = get_pregunta(self.data)
        category = pregunta["category"]
        index = pregunta["index"]
        filtered_data =  filter_by_category(self.data,category,index)
        for i in filtered_data:
            self.assertEqual(i[0],category)
            self.assertNotEqual(i[2],pregunta["question"])

    def test_possible_answers(self):
        pregunta = get_pregunta(self.data)
        category = pregunta["category"]
        index = pregunta["index"]
        filtered_data =  filter_by_category(self.data,category,index)
        possible_answers = get_possible_answers(filtered_data)
        self.assertEqual(possible_answers["raw_answer_two"][0],category)
        self.assertEqual(possible_answers["raw_answer_three"][0],category)
        self.assertNotEqual(possible_answers["answer_two"],pregunta["answer"])
        self.assertNotEqual(possible_answers["answer_three"],pregunta["answer"])

    @mock.patch('main.input', create=True)
    def test_preguntas(self, mocked_input):
        mocked_input.side_effect = [';)']
        

        mock_data = [
            ["History","i","Oompa","doo.."],
            ["History","d","Loompa","i forgot"],
            ["History","k","doompety","the rest.. doompety doo"]
        ]

        result = preguntas(self.data)
        question = result[2]
        answer = result[1]
        
        self.assertEqual(result[0], ';)')

        #non_selcted_answers = filter(lambda x: x[2]!=question,mock_data)

    def mock_imp_csv():
        return  [
            # Block 1: History
            ["A","B","C","D"],
            ["History", "i", "Oompa", "doo.."],
            ["History", "d", "Loompa", "doo.."],
            ["History", "k", "doompety", "doo.."],
            
            # Block 2: Science
            ["Science", "d", "Curie", "doo.."],
            ["Science", "d", "Murie", "doo.."],
            ["Science", "d", "Lurie", "doo.."],
            
            # Block 3: Literature
            ["Literature", "c", "Orwell", "doo.."],
            ["Literature", "c", "Or", "doo.."],
            ["Literature", "c", "well", "doo.."],
            
            # Block 4: Movies
            ["Movies", "a", "Inception", "doo.."],
            ["Movies", "a", "Memeception", "doo.."],
            ["Movies", "a", "Reception", "doo.."],
            
            # Block 5: Music
            ["Music", "b", "Queen", "doo.."],
            ["Music", "b", "Mueen", "doo.."],
            ["Music", "b", "Dueen", "doo.."]
        ]

    @mock.patch('main.input', create=True)
    @mock.patch('main.imp_csv', mock_imp_csv)
    def test_main(self, mocked_input):
        mocked_input.side_effect = ["doo..","doo..","doo..","doo..",";)"]

        result = main()
        
        self.assertEqual(result,40)
    
    # Algunos errores no se presentan en todas las partidas dado que surgen de anomalias en el csv
    # Esta funcion realiza 100 partidas para intentar detectar dichos errores.
    # IMPORTANTE: esta prueba demora 100s
    @mock.patch('main.input', create=True)
    def test_crash_detection(self, mocked_input):
        mocked_input.side_effect = list(map(str,range(500)))
        for i in range(100):
            main()

    
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)