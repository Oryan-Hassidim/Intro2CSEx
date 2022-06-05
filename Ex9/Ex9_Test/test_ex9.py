####################################################################
# Oryan Hassidim
# Oryan.Hassidim@mail.huji.ac.il
# last update: 22/05/2022  21:38
####################################################################


from random import randint, choice
import sys
from sys import executable
from os import mkdir, rmdir, getcwd, chdir
from os.path import join, isdir, isfile
import traceback
from subprocess import PIPE, run
from shutil import copyfile, rmtree
from pathlib import Path


def combination_test(car_folder, board_folder, game_folder, *tests_files):
    source_path = Path(__file__).resolve()
    source_dir = source_path.parent
    if getcwd() != source_dir:
        chdir(source_dir)
    if isdir("TESTS"):
        rmtree("TESTS")
    mkdir("TESTS")
    copyfile("helper.py", join("TESTS", "helper.py"))
    try:
        copyfile(join(car_folder, "car.py"), join("TESTS", "car.py"))
        copyfile(join(board_folder, "board.py"), join("TESTS", "board.py"))
        copyfile(join(game_folder, "game.py"), join("TESTS", "game.py"))
    except FileNotFoundError:
        rmtree("TESTS")
        return
    for test_file in tests_files:
        copyfile("_"+test_file, join("TESTS", test_file))
    out = run([executable, "-m", "pytest",  "TESTS"], shell=True)
    rmtree("TESTS")
    if out.returncode != 0:
        raise Exception("pytest failed\n")


def wcar_test(A_or_B_or_C):
    combination_test("W", A_or_B_or_C, A_or_B_or_C,
                     "test_wcar_board.py", "test_wcar_game.py")


def wboard_test(A_or_B_or_C):
    combination_test(A_or_B_or_C, "W", A_or_B_or_C,
                     "test_wboard_game.py")


def wcar_wboard_test(A_or_B_or_C):
    combination_test("W", "W", A_or_B_or_C,
                     "test_wcar_wboard_game.py")

#######################   REGULAR   #######################


def test_AAA():
    combination_test("A", "A", "A",
                     "test_car.py", "test_board.py", "test_game.py")


def test_BBB():
    combination_test("B", "B", "B",
                     "test_car.py", "test_board.py", "test_game.py")


def test_CCC():
    combination_test("C", "C", "C",
                     "test_car.py", "test_board.py", "test_game.py")

#######################   wcar & wboard   #######################


def test_wcar_A():
    wcar_test("A")


def test_wboard_A():
    wboard_test("A")


def test_wcar_wboard_A():
    wcar_wboard_test("A")


def test_wcar_B():
    wcar_test("B")


def test_wboard_B():
    wboard_test("B")


def test_wcar_wboard_B():
    wcar_wboard_test("B")


def test_wcar_C():
    wcar_test("C")


def test_wboard_C():
    wboard_test("C")


def test_wcar_wboard_C():
    wcar_wboard_test("C")

#######################   combinations   #######################


def test_AAB():
    combination_test("A", "A", "B",
                     "test_game.py")


def test_AAC():
    combination_test("A", "A", "C",
                     "test_game.py")


def test_ABA():
    combination_test("A", "B", "A",
                     "test_board.py", "test_game.py")


def test_ABB():
    combination_test("A", "B", "B",
                     "test_board.py", "test_game.py")


def test_ABC():
    combination_test("A", "B", "C",
                     "test_board.py", "test_game.py")


def test_ACA():
    combination_test("A", "C", "A",
                     "test_board.py", "test_game.py")


def test_ACB():
    combination_test("A", "C", "B",
                     "test_board.py", "test_game.py")


def test_ACC():
    combination_test("A", "C", "C",
                     "test_board.py", "test_game.py")


def test_BAA():
    combination_test("B", "A", "A",
                     "test_board.py", "test_game.py")


def test_BAB():
    combination_test("B", "A", "B",
                     "test_board.py", "test_game.py")


def test_BAC():
    combination_test("B", "A", "C",
                     "test_board.py", "test_game.py")


def test_BBA():
    combination_test("B", "B", "A",
                     "test_game.py")


def test_BBC():
    combination_test("B", "B", "C",
                     "test_game.py")


def test_BCA():
    combination_test("B", "C", "A",
                     "test_board.py", "test_game.py")


def test_BCB():
    combination_test("B", "C", "B",
                     "test_board.py", "test_game.py")


def test_BCC():
    combination_test("B", "C", "C",
                     "test_board.py", "test_game.py")


def test_CAA():
    combination_test("C", "A", "A",
                     "test_board.py", "test_game.py")


def test_CAB():
    combination_test("C", "A", "B",
                     "test_board.py", "test_game.py")


def test_CAC():
    combination_test("C", "A", "C",
                     "test_board.py", "test_game.py")


def test_CBA():
    combination_test("C", "B", "A",
                     "test_board.py", "test_game.py")


def test_CBB():
    combination_test("C", "B", "B",
                     "test_board.py", "test_game.py")


def test_CBC():
    combination_test("C", "B", "C",
                     "test_board.py", "test_game.py")


def test_CCA():
    combination_test("C", "C", "A",
                     "test_game.py")


def test_CCB():
    combination_test("C", "C", "B",
                     "test_game.py")

#combinations = [car + board + game for car in "ABC" for board in "ABC" for game in "ABC"]
# for c, b, g in combinations:
#    if c == b == g:
#        continue
#    if c == b:
#        print(f"""def test_{c}{b}{g}():
#    combination_test("{c}", "{b}", "{g}",
#                     "test_game.py")""")
#    else:
#        print(f"""def test_{c}{b}{g}():
#    combination_test("{c}", "{b}", "{g}",
#                     "test_board.py", "test_game.py")""")


def run_test(name, func):
    try:
        func()
        print(f"\033[1;32m{name} test PASSED\033[0m")
        return 1
    except Exception as e:
        print(
            f"\033[1;31m{name} test FAILED\n\t{type(e).__name__}: {e}\033[0m")
        print(traceback.format_exc())
    print("\033[0m", end="")
    return 0


def main():
    source_path = Path(__file__).resolve()
    source_dir = source_path.parent
    if getcwd() != source_dir:
        chdir(source_dir)
    if "min" in sys.argv:
        tests = [
            "test_AAA",
            "test_BBB",
            "test_CCC",
            "test_wcar_A",
            "test_wboard_A",
            "test_wcar_wboard_A",
            "test_wcar_B",
            "test_wboard_B",
            "test_wcar_wboard_B",
            "test_wcar_C",
            "test_wboard_C",
            "test_wcar_wboard_C",
        ]
    else:
        tests = [
            "test_AAA",
            "test_BBB",
            "test_CCC",
            "test_wcar_A",
            "test_wboard_A",
            "test_wcar_wboard_A",
            "test_wcar_B",
            "test_wboard_B",
            "test_wcar_wboard_B",
            "test_wcar_C",
            "test_wboard_C",
            "test_wcar_wboard_C",
            "test_AAB",
            "test_AAC",
            "test_ABA",
            "test_ABB",
            "test_ABC",
            "test_ACA",
            "test_ACB",
            "test_ACC",
            "test_BAA",
            "test_BAB",
            "test_BAC",
            "test_BBA",
            "test_BBC",
            "test_BCA",
            "test_BCB",
            "test_BCC",
            "test_CAA",
            "test_CAB",
            "test_CAC",
            "test_CBA",
            "test_CBB",
            "test_CBC",
            "test_CCA",
            "test_CCB"
        ]
    count = 0
    for test in tests:
        count += run_test(test, globals()[test])
    print()
    if count == len(tests):
        print("\033[1;32m==============All OK==============")
    else:
        print(f"\033[1;31m========={count}/{len(tests)} tests passed=========")
    print("\033[0m")


if __name__ == "__main__":
    sys.exit(int(main() or 0))
