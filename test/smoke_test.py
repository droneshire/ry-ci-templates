from ry_ci_templates import __doc__


def test_module_imports() -> None:
    assert __doc__ is not None
