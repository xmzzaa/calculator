import pytest


def test_returnSignal(controller):
    """Tests the Return key binding interface to our Qt display widget."""
    from PyQt5 import QtCore, QtGui

    controller._view.setDisplayText("1+2")
    event = QtGui.QKeyEvent(
        QtCore.QEvent.KeyPress, QtCore.Qt.Key_Enter, QtCore.Qt.NoModifier
    )
    controller._view.display.keyPressEvent(event)
    assert controller._view.displayText() == "3"

def test_calculateResult(controller):
    controller._view.setDisplayText("1+2")
    controller._calculateResult()
    assert controller._view.displayText() == "3"


@pytest.mark.parametrize("a, b", [(4, 3), (1, 2)])
def test_calculateResult_mult(controller, a, b):
    controller._view.setDisplayText(str(a) + "+" + str(b))
    controller._calculateResult()
    assert controller._view.displayText() == str(a + b)
