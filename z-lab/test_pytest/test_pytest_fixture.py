#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_pytest_fixture.py
@Time   :   2021/7/1 14:24
@Contact    :
@Author     :   WG
@Version    :   v 0.1
@Desc   :
"""
import pytest


#
#
from testcases.conftest import Fruit


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()
#
# Arrange
@pytest.fixture
def fruit_bowl():
    from testcases.conftest import Fruit
    fruit = Fruit("apple")
    return fruit

@pytest.mark.usefixtures("fruit_bowl")
def test_fruit_salad():
    # Act
    fruit_salad = FruitSalad()
    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)