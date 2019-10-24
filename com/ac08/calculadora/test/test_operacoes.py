"""Arquivo de teste das funções"""
from com.ac08.calculadora import operacoes


def test_soma():
    """Testando a função soma"""
    assert operacoes.soma(6, 6) == 12, "Should be 12"


def test_sub():
    """Testando a função subtração"""
    assert operacoes.subt(6, 6) == 0, "Should be 0"


def test_mult():
    """Testando a função multiplicação"""
    assert operacoes.mult(7, 3) == 21, "Should be 21"


def test_div():
    """Testando a função divisão"""
    assert operacoes.divi(14, 2) == 7, "Should be 7"
