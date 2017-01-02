def get_regexps_for_language(language_code, base_regexps, i18n_regexps):
    """
    Return the regular expressions that should be applied based on the given `language_code`. `language_code` can
    either be a language code with a variant, eg. `fr-ch`, or a language without any variant, eg. `fr`. In the case of
    a language code with a variant, all the regexps from the variant-free language code (eg. `fr`) will be taken, along
    with all regexps from the language code with a variant.

    Practically this means that the `fr` language code would include only `fr` regexps, whereas the `fr-ch` language
    code would include both the `fr` and the `fr-ch` regexps.
    """
    language_code = language_code.lower()

    try:
        language, variant = language_code.split('-', 1)
    except ValueError:
        # If the split could not be done, it means there's no variant in `language_code`
        language = language_code
        variant = None

    regexps_to_apply = base_regexps + i18n_regexps.get(language, [])

    if variant:
        regexps_to_apply += i18n_regexps.get(language_code, [])

    return regexps_to_apply
