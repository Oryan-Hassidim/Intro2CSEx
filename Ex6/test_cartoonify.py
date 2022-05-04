###################################################
# Oryan Hassidim
# Oryan.Hassidim@mail.huji.ac.il
# last update: 02/05/2022 22:30
###################################################

from cartoonify import (
    separate_channels,
    combine_channels,
    RGB2grayscale,
    blur_kernel,
    apply_kernel,
    bilinear_interpolation,
    resize,
    scale_down_colored_image,
    rotate_90,
    get_edges,
    quantize,
    add_mask,
    cartoonify
)
from random import randint
import subprocess
import sys


def test_separate_channels():
    assert separate_channels([[[1, 2]]]) == [[[1]], [[2]]]
    assert separate_channels([[[1, 2, 3]] * 3] * 4) == [
        [[1] * 3] * 4,
        [[2] * 3] * 4,
        [[3] * 3] * 4,
    ]


def test_combine_channels():
    assert combine_channels([[[1]], [[2]]]) == [[[1, 2]]]
    assert (
        combine_channels([[[1] * 3] * 4, [[2] * 3] * 4, [[3] * 3] * 4])
        == [[[1, 2, 3]] * 3] * 4
    )


def test_RGB2grayscale():
    assert RGB2grayscale([[[100, 180, 240]]]) == [[163]]
    assert RGB2grayscale([[[200, 0, 14], [15, 6, 50]]]) == [[61, 14]]


def test_blur_kernel():
    assert blur_kernel(3) == [
        [1 / 9, 1 / 9, 1 / 9],
        [1 / 9, 1 / 9, 1 / 9],
        [1 / 9, 1 / 9, 1 / 9],
    ]
    assert blur_kernel(7) == [[1/49]*7]*7


def test_apply_kernel():
    assert apply_kernel([[0, 128, 255]], blur_kernel(3)) == [[14, 128, 241]]
    assert apply_kernel(
        [
            [10, 20, 30, 40, 50],
            [8, 16, 24, 32, 40],
            [6, 12, 18, 24, 30],
            [4, 8, 12, 16, 20],
        ],
        blur_kernel(5),
    ) == [
        [12, 20, 26, 34, 44],
        [11, 17, 22, 27, 34],
        [10, 16, 20, 24, 29],
        [7, 11, 16, 18, 21],
    ]
    assert apply_kernel([[1, 1, 1]], [[1]*3]*3) == [[9, 9, 9]]
    assert apply_kernel([[1, 1, 1]], [[0]*3]*3) == [[0, 0, 0]]
    assert apply_kernel([[1,2,3]], [[0]*3, [0, 1, 0], [0]*3]) == [[1,2,3]]
    assert apply_kernel([[1,2,3]], [[0]*3, [0, 0, 1], [0]*3]) == [[2,3,3]]


def test_bilinear_interpolation():
    assert bilinear_interpolation([[0, 64], [128, 255]], 0, 0) == 0
    assert bilinear_interpolation([[0, 64], [128, 255]], 1, 1) == 255
    assert bilinear_interpolation([[0, 64], [128, 255]], 0.5, 0.5) == 112
    assert bilinear_interpolation([[0, 64], [128, 255]], 0.5, 1) == 160


def test_resize():
    assert resize([[0, 10], [10, 0]], 2, 2) == [[0, 10], [10, 0]]
    assert resize([[0, 10], [10, 0]], 3, 3) == [
        [0, 5, 10], [5, 5, 5], [10, 5, 0]]
    assert resize([[0, 5, 10], [5, 5, 5], [10, 5, 0]],
                  2, 2) == [[0, 10], [10, 0]]
    mat = [[2, 4, 6],
           [3, 8, 12],
           [16, 5, 11]]
    assert resize(mat, 2, 2) == [[2, 6], [16, 11]]
    assert resize(mat, 6, 6) == [[2, 3, 4, 4, 5, 6], [2, 4, 5, 6, 7, 8], [
        3, 5, 6, 8, 9, 11], [6, 6, 7, 8, 10, 12], [11, 9, 7, 7, 9, 11], [16, 12, 7, 6, 9, 11]]
    assert resize(mat, 3, 6) == [[2, 3, 4, 4, 5, 6], [
        3, 5, 7, 9, 10, 12], [16, 12, 7, 6, 9, 11]]
    assert resize(mat, 6, 3) == [[2, 4, 6], [2, 6, 8], [
        3, 7, 11], [6, 7, 12], [11, 6, 11], [16, 5, 11]]
    assert resize(mat, 4, 4) == [[2, 3, 5, 6], [
        3, 5, 8, 10], [7, 7, 9, 12], [16, 9, 7, 11]]


def test_scale_down_colored_image():
    assert scale_down_colored_image(
        [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], 2) == None
    assert scale_down_colored_image([[[1, 2, 3], [4, 5, 6]]], 2) == None
    assert scale_down_colored_image([[[1, 2, 3]], [[7, 8, 9]]], 2) == None
    pix = [0] * 3
    row = [pix] * 6
    im = [row] * 6
    assert scale_down_colored_image(im, 2) == [[pix] * 2] * 2
    im = [row] * 9
    assert scale_down_colored_image(im, 3) == [[pix] * 2] * 3
    test_resize()
    test_separate_channels()
    test_combine_channels()
    r = range
    im = [[[randint(0, 256) for _ in 'RGB'] for _ in r(30)] for _ in r(60)]
    channels = separate_channels(im)
    expected = [resize(c, 10, 5) for c in channels]
    expected = combine_channels(expected)
    assert scale_down_colored_image(im, 10) == expected


def test_rotate_90():
    assert rotate_90([[1, 2, 3], [4, 5, 6]], 'R') == [[4, 1], [5, 2], [6, 3]]
    assert rotate_90([[1, 2, 3], [4, 5, 6]], 'L') == [[3, 6], [2, 5], [1, 4]]
    assert rotate_90([[[1, 2, 3], [4, 5, 6]], [[0, 5, 9], [255, 200, 7]]], 'L') == [
        [[4, 5, 6], [255, 200, 7]], [[1, 2, 3], [0, 5, 9]]]


def test_get_edges():
    assert get_edges([[200, 50, 200]], 3, 3, 10) == [[255, 0, 255]]


def test_quantize():
    assert quantize([[0, 50, 100], [150, 200, 250]], 8) == [
        [0, 36, 109], [146, 219, 255]]


def test_add_mask():
    assert add_mask([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]],
                    [[[250, 250, 250], [0, 0, 0]], [[250, 250, 100], [1, 11, 13]]],
                    [[0, 0.5, 1]]*2) == [[[250, 250, 250], [2, 2, 3]], [[250, 250, 100], [6, 11, 12]]]
    assert add_mask([[50, 50, 50]], [[200, 200, 200]],
                    [[0, 0.5, 1]]) == [[200, 125, 50]]


def test_cartoonify():
    assert cartoonify([[[50, 150, 250]]], 3, 3, 20, 8) == [
        [[36, 146, 255]]]
    assert cartoonify([[[0]*3]], 3, 3, 3, 2) == [[[0, 0, 0]]]


def test_params_check():
    executable = sys.executable
    res = subprocess.run([executable,
                          "cartoonify.py"], shell=True, stdout=subprocess.PIPE)
    assert any(map(res.stdout.decode("utf-8").strip().count,
                   ["param", "arg", "7", "8"])), "Check params number!!"
    res = subprocess.run([executable,
                          "cartoonify.py",
                          "ziggy.png"], shell=True, stdout=subprocess.PIPE)
    assert any(map(res.stdout.decode("utf-8").strip().count,
                   ["param", "arg", "7", "8"])), "Check params number!!"
    res = subprocess.run([executable,
                          "cartoonify.py",
                          "ziggy.png", "cartoon.png",
                          "200", "3", "3", "3"], shell=True, stdout=subprocess.PIPE)
    assert any(map(res.stdout.decode("utf-8").strip().count,
                   ["param", "arg", "7", "8"])), "Check params number!!"


def run_test(name, func):
    try:
        func()
        print(f"\033[1;32m{name} test PASSED")
        return 1
    except MypyTypesError as e:
        print(f"\033[1;31m{name} test FAILED\n\t{type(e).__name__}: {e}")
    except Exception as e:
        print(f"\033[1;31m{name} test FAILED\n\t{type(e).__name__}: {e}")
        print(traceback.format_exc())
    return 0


def main():
    tests = [
        "separate_channels",
        "combine_channels",
        "RGB2grayscale",
        "blur_kernel",
        "apply_kernel",
        "bilinear_interpolation",
        "resize",
        "scale_down_colored_image",
        "rotate_90",
        "get_edges",
        "quantize",
        "add_mask",
        "cartoonify",
        "params_check"]
    count = 0
    for test in tests:
        count += run_test(test, globals()["test_" + test])
    print()
    if count == len(tests):
        print("\033[1;32m==============All OK==============")
    else:
        print(f"\033[1;31m========={count}/{len(tests)} tests passed=========")
    print("\033[0m")


if __name__ == "__main__":
    sys.exit(int(main() or 0))
