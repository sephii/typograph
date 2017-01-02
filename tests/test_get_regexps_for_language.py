from typograph.i18n import get_regexps_for_language


def test_language_without_variant():
    assert 'foo' in get_regexps_for_language('fr', [], {'fr': ['foo']})


def test_language_with_variant():
    assert 'foo' in get_regexps_for_language('fr-ch', [], {'fr': ['foo']})


def test_language_with_variant_not_in_i18n_regexps():
    assert 'foo' not in get_regexps_for_language('fr-ch', [], {'fr-fr': ['foo']})


def test_base_regexps_always_returned():
    assert get_regexps_for_language('fr', ['foo'], {'fr': ['bar']}) == ['foo', 'bar']
