import pytest
from domain.entities.resources import CodeContent
from domain.exceptions.values import EmptyTextException, InvalidCodeSyntaxException


def test_code_content_value_object_creation_success():
    """Testing successfull AST-validation pass on correct Python code."""

    valid_code = """
import asyncio

async def get_users():
    return {"status": "ok"}
"""
    vo = CodeContent.from_raw(body=valid_code, lang="python")

    assert vo.body == valid_code.replace("\r\n", "\n")
    assert len(vo.checksum) == 64  # SHA-256 хэш


def test_code_content_value_object_creation_raises_empty_exception():
    """Testing validation fail on empty string or only spaces string."""
    with pytest.raises(EmptyTextException):
        CodeContent.from_raw(body="   \n   ", lang="python")


def test_code_content_value_object_creation_raises_syntax_exception():
    """Testing error trigger on corrupt syntax (unclosed bracket for example)."""
    invalid_code = """
def broken_function():
    print("Забыли закрыть скобку"
"""
    with pytest.raises(InvalidCodeSyntaxException) as exc_info:
        CodeContent.from_raw(body=invalid_code, lang="python")

    assert "Invalid Python syntax" in str(exc_info.value)
