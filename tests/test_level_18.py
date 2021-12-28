import hedy
import textwrap
from test_level_01 import HedyTester

class TestsLevel18(HedyTester):
    level = 18

    def test_print_brackets(self):
      code = textwrap.dedent("""\
      print('Hallo!')""")

      expected = textwrap.dedent("""\
      print(f'Hallo!')""")

      self.multi_level_tester(
        code=code,
        expected=expected,
        extra_check_function=self.is_not_turtle(),
        expected_commands=['print']
      )

    def test_print_var_brackets(self):
        code = textwrap.dedent("""\
        naam is 'Hedy'
        print('ik heet', naam)""")

        expected = textwrap.dedent("""\
        naam = 'Hedy'
        print(f'ik heet{naam}')""")

        self.multi_level_tester(
          code=code,
          expected=expected,
          extra_check_function=self.is_not_turtle()
        )

    def test_input(self):
        code = textwrap.dedent("""\
        leeftijd is input('Hoe oud ben jij?')
        print(leeftijd)""")
        expected = textwrap.dedent("""\
        leeftijd = input(f'Hoe oud ben jij?')
        try:
          leeftijd = int(leeftijd)
        except ValueError:
          try:
            leeftijd = float(leeftijd)
          except ValueError:
            pass
        print(f'{leeftijd}')""")

        self.multi_level_tester(
          max_level=20,
          code=code,
          expected=expected,
          extra_check_function=self.is_not_turtle()
        )

    def test_if_with_equals_sign(self):
      code = textwrap.dedent("""\
      naam is 'Hedy'
      if naam == Hedy:
          print('koekoek')""")

      expected = textwrap.dedent("""\
      naam = 'Hedy'
      if str(naam) == str('Hedy'):
        print(f'koekoek')""")

      self.single_level_tester(code=code, expected=expected)

    # issue also in level 17, leaving for now.
    # def test_bigger(self):
    #     code = textwrap.dedent("""\
    #     leeftijd is input('Hoe oud ben jij?')
    #     if leeftijd > 12:
    #         print('Dan ben je ouder dan ik!')""")
    #     expected = textwrap.dedent("""\
    #     leeftijd = input('Hoe oud ben jij?')
    #     if int(leeftijd) > int('12'):
    #       print(f'Dan ben je ouder dan ik!')""")
    #
    #     self.multi_level_tester(
    #       code=code,
    #       expected=expected,
    #       extra_check_function=self.is_not_turtle(),
    #       test_name=self.name()
    #     )
    # def test_big_and_small(self):
    #     code = textwrap.dedent("""\
    #     leeftijd is input('Hoe oud ben jij?')
    #     if leeftijd < 12:
    #         print('Dan ben je jonger dan ik!')
    #     elif leeftijd > 12:
    #         print('Dan ben je ouder dan ik!')""")
    #     expected = textwrap.dedent("""\
    #     leeftijd = input('Hoe oud ben jij?')
    #     if int(leeftijd) < int('12'):
    #       print(f'Dan ben je jonger dan ik!')
    #     elif int(leeftijd) > int('12'):
    #       print(f'Dan ben je ouder dan ik!')""")
    #
    #     self.multi_level_tester(
    #       max_level=20,
    #       code=code,
    #       expected=expected,
    #       extra_check_function=self.is_not_turtle(),
    #       test_name=self.name()
    #     )

    def test_if_else(self):
      code = textwrap.dedent("""\
      antwoord is input('Hoeveel is 10 plus 10?')
      if antwoord is 20:
          print('Goedzo!')
          print('Het antwoord was inderdaad', antwoord)
      else:
          print('Foutje')
          print('Het antwoord moest zijn', antwoord)""")

      expected = textwrap.dedent("""\
      antwoord = input(f'Hoeveel is 10 plus 10?')
      try:
        antwoord = int(antwoord)
      except ValueError:
        try:
          antwoord = float(antwoord)
        except ValueError:
          pass
      if str(antwoord) == str('20'):
        print(f'Goedzo!')
        print(f'Het antwoord was inderdaad{antwoord}')
      else:
        print(f'Foutje')
        print(f'Het antwoord moest zijn{antwoord}')""")

      self.multi_level_tester(
        code=code,
        expected=expected,
        expected_commands=['input', 'if', 'print', 'print', 'print', 'print'],
        extra_check_function=self.is_not_turtle()
      )

    def test_for_loop(self):
      code = textwrap.dedent("""\
      a is 2
      b is 3
      for a in range(2,4):
        a is a + 2
        b is b + 2""")
      expected = textwrap.dedent("""\
      a = 2
      b = 3
      step = 1 if int(2) < int(4) else -1
      for a in range(int(2), int(4) + step, step):
        a = a + 2
        b = b + 2
        time.sleep(0.1)""")

      self.multi_level_tester(
        code=code,
        expected=expected,
        extra_check_function=self.is_not_turtle()
      )

    def test_for_nesting(self):
      code = textwrap.dedent("""\
      for i in range(1, 3):
        for j in range(1,4):
          print('rondje: ', i, ' tel: ', j)""")
      expected = textwrap.dedent("""\
      step = 1 if int(1) < int(3) else -1
      for i in range(int(1), int(3) + step, step):
        step = 1 if int(1) < int(4) else -1
        for j in range(int(1), int(4) + step, step):
          print(f'rondje: {i} tel: {j}')
          time.sleep(0.1)""")

      self.multi_level_tester(

        code=code,
        expected=expected,
        extra_check_function=self.is_not_turtle()
      )

    def test_input_with_list(self):
      code = textwrap.dedent("""
      color is ['green', 'blue']
      choice is input('Is your favorite color one of: ' color)""")

      expected = textwrap.dedent("""\
      color = ['green', 'blue']
      choice = input(f'Is your favorite color one of: {color}')
      try:
        choice = int(choice)
      except ValueError:
        try:
          choice = float(choice)
        except ValueError:
          pass""")

      self.multi_level_tester(
          code=code,
          expected=expected,
          extra_check_function=self.is_not_turtle()
      )

    # negative tests
    def test_var_undefined_error_message(self):
      code = textwrap.dedent("""\
        naam is 'Hedy'
        print('ik heet ', name)""")

      self.multi_level_tester(
        code=code,
        exception=hedy.exceptions.UndefinedVarException
      )

      # deze extra check functie kan nu niet mee omdat die altijd op result werkt
      # evt toch splitsen in 2 (pos en neg?)
      # self.assertEqual('name', context.exception.arguments['name'])