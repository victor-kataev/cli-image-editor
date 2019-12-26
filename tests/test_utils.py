from pytest import fixture
import numpy as np
from numpy.testing import assert_equal, assert_raises, assert_array_equal
from PIL import Image
from core import utils


@fixture
def image():
    return np.asarray(Image.open('tests/lenna.png'), dtype=np.uint8)


@fixture
def image_bw():
    return np.asarray(Image.open('tests/lenna-bw.png'), dtype=np.uint8)


@fixture
def image_bw_inverse():
    return np.asarray(Image.open('tests/lenna-bw-inverse.png'), dtype=np.uint8)


@fixture
def image_bw_inverse_sharpen():
    return np.asarray(Image.open('tests/lenna-bw-inverse-sharpen.png'), dtype=np.uint8)


@fixture
def image_bw_inverse_sharpen_mirror():
    return np.asarray(Image.open('tests/lenna-bw-inverse-sharpen-mirror.png'), dtype=np.uint8)


@fixture
def image_darken_25():
    return np.asarray(Image.open('tests/lenna-darken-25.png'), dtype=np.uint8)


@fixture
def image_darken_25_sharpen():
    return np.asarray(Image.open('tests/lenna-darken-25-sharpen.png'), dtype=np.uint8)


@fixture
def image_inverse():
    return np.asarray(Image.open('tests/lenna-inverse.png'), dtype=np.uint8)


@fixture
def image_lighten_25():
    return np.asarray(Image.open('tests/lenna-lighten-25.png'), dtype=np.uint8)


@fixture
def image_lighten_25_sharpen():
    return np.asarray(Image.open('tests/lenna-lighten-25-sharpen.png'), dtype=np.uint8)


@fixture
def image_mirror():
    return np.asarray(Image.open('tests/lenna-mirror.png'), dtype=np.uint8)


@fixture
def image_mirror_rotate():
    return np.asarray(Image.open('tests/lenna-mirror-rotate.png'), dtype=np.uint8)


@fixture
def image_sharpen():
    return np.asarray(Image.open('tests/lenna-sharpen.png'), dtype=np.uint8)


@fixture
def image_sharpen_inverse():
    return np.asarray(Image.open('tests/lenna-sharpen-inverse.png'), dtype=np.uint8)


@fixture
def image_bw_lighten_25():
    return np.asarray(Image.open('tests/lenna-bw-lighten-25.png'), dtype=np.uint8)


@fixture
def image_bw_darken_25():
    return np.asarray(Image.open('tests/lenna-bw-darken-25.png'), dtype=np.uint8)


def test_bw(image, image_bw):
    assert_equal(image_bw, utils.bw(image).astype(np.uint8))


def test_bw_inverse(image, image_bw_inverse):
    bw = utils.bw(image)
    bw_inverse = utils.inverse(bw)
    assert_equal(image_bw_inverse, bw_inverse.astype(np.uint8))


def test_bw_inverse_sharpen(image, image_bw_inverse_sharpen):
    bw = utils.bw(image)
    bw_inverse = utils.inverse(bw)
    bw_inverse_sharpen = utils.sharpen(bw_inverse)
    assert_equal(image_bw_inverse_sharpen, bw_inverse_sharpen.astype(np.uint8))


def test_bw_inverse_sharpen_mirror(image, image_bw_inverse_sharpen_mirror):
    bw = utils.bw(image)
    bw_inverse = utils.inverse(bw)
    bw_inverse_sharpen = utils.sharpen(bw_inverse)
    bw_inverse_sharpen_mirror = utils.mirror(bw_inverse_sharpen)
    assert_equal(image_bw_inverse_sharpen_mirror, bw_inverse_sharpen_mirror.astype(np.uint8))


def test_darken_25(image, image_darken_25):
    assert_equal(image_darken_25, utils.darken(image, 25).astype(np.uint8))


def test_darken_25_sharpen(image, image_darken_25_sharpen):
    darken_25 = utils.darken(image, 25).astype(np.uint8)
    darken_25_sharpen = utils.sharpen(darken_25)
    assert_equal(image_darken_25_sharpen, darken_25_sharpen)


def test_inverse(image, image_inverse):
    assert_equal(image_inverse, utils.inverse(image))


def test_lighten_25(image, image_lighten_25):
    assert_equal(image_lighten_25, utils.lighten(image, 25))


def test_lighten_25_sharpen(image, image_lighten_25_sharpen):
    lighten_25 = utils.lighten(image, 25)
    lighten_25_sharpen = utils.sharpen(lighten_25)
    assert_equal(image_lighten_25_sharpen, lighten_25_sharpen)


def test_bw_lighten_25(image, image_bw_lighten_25):
    bw = utils.bw(image)
    bw_lighten_25 = utils.lighten(bw, 25)
    assert_equal(image_bw_lighten_25, bw_lighten_25.astype(np.uint8))


def test_bw_darken_25(image, image_bw_darken_25):
    bw = utils.bw(image)
    bw_darken_25 = utils.darken(bw, 25)
    assert_equal(image_bw_darken_25, bw_darken_25.astype(np.uint8))


def test_mirror(image, image_mirror):
    assert_equal(image_mirror, utils.mirror(image))


def test_mirror_rotate(image, image_mirror_rotate):
    mirror = utils.mirror(image)
    mirror_rotate = utils.rotate(mirror)
    assert_equal(image_mirror_rotate, mirror_rotate)
    rotate = utils.rotate(image)
    rotate_mirror = utils.mirror(rotate)
    assert_raises(AssertionError, assert_array_equal, image_mirror_rotate, rotate_mirror)


def test_sharpen(image, image_sharpen):
    assert_equal(image_sharpen, utils.sharpen(image))


def test_sharpen_inverse(image, image_sharpen_inverse):
    sharpen = utils.sharpen(image)
    sharpen_inverse = utils.inverse(sharpen)
    assert_equal(image_sharpen_inverse, sharpen_inverse)
