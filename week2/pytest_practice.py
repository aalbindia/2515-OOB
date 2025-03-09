from obscure import obscure_text

def test_obscure_text():
    assert obscure_text('Hello World') == 'H3||0 W0r|d'