# -*- coding: utf-8 -*-
#
# MCR-Analyser
#
# Copyright (C) 2021 Martin Knopp, Technical University of Munich
#
# This program is free software, see the LICENSE file in the root of this
# repository for details

"""Interface and classes for spot analysis."""

from abc import ABCMeta, abstractmethod

import numpy as np


class Spot(metaclass=ABCMeta):
    """Base class defining spot analysis interface."""

    def __init__(self, data: np.ndarray):
        """Initialize spot object.

        :param data: (np.ndarray) Pixel data of the spot in question.
        """
        self.img = data

    @abstractmethod
    def value(self) -> float:
        """Return chemiluminescence value of the spot."""
        pass


class DeviceBuiltin(Spot):
    """Spot analysis class replicating MCR-Rs internal behaviour."""

    def value(self) -> float:
        """Return mean of the 10 brightest pixels."""
        vals = np.sort(self.img, axis=None)
        return np.mean(vals[-10:])
