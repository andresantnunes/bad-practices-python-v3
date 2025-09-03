import sys
import random
from typing import List, Optional
import unittest

#
# SOLID - Principio da Responsabilidade Unica (SRP)
# Classes com responsabilidades claras. Uma para o Aluno e outra para a Turma.
#
class Student:
    """Representa um aluno com um ID e nome."""
    def __init__(self, student_id: int, name: str):
        self.student_id = student_id
        self.name = name

    def __repr__(self) -> str:
        return f"Student(id={self.student_id}, name='{self.name}')"

class Lesson:
    """Representa uma aula com um ID e um professor, seguindo a lógica do usuário."""
    def __init__(self, lesson_id: int, teacher: 'Teacher'):
        self.lesson_id = lesson_id
        self.teacher = teacher

    def __repr__(self) -> str:
        return f"Lesson(id={self.lesson_id}, teacher='{self.teacher.name}')"

class Teacher:
    """Representa um professor."""
    def __init__(self, teacher_id: int, name: str):
        self.teacher_id = teacher_id
        self.name = name

#
# SOLID - Principio da Inversao de Dependencia (DIP)
# O repositório de dados é uma abstração, permitindo que a lógica de negócio
# nao dependa de uma implementacao de banco de dados especifica.
#
class LessonRepository:
    """Gerencia as operacoes de persistencia das aulas."""

    def __init__(self, initial_lessons: Optional[List[Lesson]] = None):
        self._lessons = initial_lessons if initial_lessons is not None else []

    def add(self, lesson: Lesson) -> None:
        if any(l.lesson_id == lesson.lesson_id for l in self._lessons):
            print(f"Lesson with ID {lesson.lesson_id} already exists.")
            return
        self._lessons.append(lesson)

    def get_by_id(self, lesson_id: int) -> Optional[Lesson]:
        return next((l for l in self._lessons if l.lesson_id == lesson_id), None)

    def get_all(self) -> List[Lesson]:
        return self._lessons

    def remove(self, lesson_id: int) -> None:
        self._lessons = [l for l in self._lessons if l.lesson_id != lesson_id]

class Program:
    """Gerencia a logica de negocio e a interacao com o usuario."""

    def __init__(self, repository: LessonRepository):
        self.repository = repository

    def create_lesson_with_teacher(self, lesson_id: int, teacher_name: str) -> None:
        teacher = Teacher(random.randint(100, 999), teacher_name)
        lesson = Lesson(lesson_id, teacher)
        self.repository.add(lesson)

    def run(self):
        print("Programa de Gerenciamento de Aulas (Versao Correta)")
        while True:
            print("\nEscolha uma opcao:")
            print("1. Criar Aula")
            print("2. Buscar Aula")
            print("3. Listar Todas as Aulas")
            print("4. Sair")

            try:
                opcao = input("Digite sua opcao: ")
                if opcao == "1":
                    lesson_id = int(input("Digite o ID da aula: "))
                    teacher_name = input("Digite o nome do professor: ")
                    self.create_lesson_with_teacher(lesson_id, teacher_name)
                    print(f"Aula com ID {lesson_id} criada com sucesso!")
                elif opcao == "2":
                    lesson_id = int(input("Digite o ID da aula: "))
                    lesson_found = self.repository.get_by_id(lesson_id)
                    if lesson_found:
                        print(f"Aula encontrada: {lesson_found}")
                    else:
                        print("Aula nao encontrada.")
                elif opcao == "3":
                    all_lessons = self.repository.get_all()
                    if not all_lessons:
                        print("Nenhuma aula criada.")
                    else:
                        for lesson in all_lessons:
                            print(f"ID: {lesson.lesson_id}, Professor: {lesson.teacher.name}")
                elif opcao == "4":
                    print("Saindo...")
                    sys.exit(0)
                else:
                    print("Opcao invalida.")
            except ValueError:
                print("Entrada invalida. Por favor, digite um numero.")

# Testes unitarios
class TestLessonProgram(unittest.TestCase):
    def setUp(self):
        self.repository = LessonRepository()
        self.program = Program(self.repository)

    def test_create_lesson(self):
        self.program.create_lesson_with_teacher(1, "Professor A")
        lesson = self.repository.get_by_id(1)
        self.assertIsNotNone(lesson)
        self.assertEqual(lesson.teacher.name, "Professor A")
    
    def test_create_duplicate_lesson_id(self):
        self.program.create_lesson_with_teacher(1, "Professor A")
        self.program.create_lesson_with_teacher(1, "Professor B")
        lessons = self.repository.get_all()
        self.assertEqual(len(lessons), 1)

    def test_get_non_existent_lesson(self):
        lesson = self.repository.get_by_id(999)
        self.assertIsNone(lesson)

if __name__ == '__main__':
    # Este bloco executa os testes se o arquivo for executado com `python nome_do_arquivo.py`
    # E executa o programa principal se for executado diretamente.
    if 'unittest' in sys.argv:
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    else:
        repository = LessonRepository()
        program = Program(repository)
        program.run()
