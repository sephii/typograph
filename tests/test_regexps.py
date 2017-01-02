from typograph import get_typograph


def test_base_fr_regexps_turn_quotes_into_guillemets():
    assert get_typograph('fr')('"foo"') == '« foo »'


def test_base_fr_regexps_adds_nbsp_before_punctuation():
    assert get_typograph('fr')('hello! world?') == 'hello ! world ?'


def test_html_parsing_strips_body():
    assert get_typograph('fr', html_parser=None)('<html><body><p>"hello"</p></body></html>', is_html=True) == '<p>« hello »</p>'
