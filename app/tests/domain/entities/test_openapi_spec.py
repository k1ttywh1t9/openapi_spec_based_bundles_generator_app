from datetime import datetime

import pytest

from domain.entities.specs import OpenAPISpec


def test_create_openapi_spec_success_dummy_data():
    given_data = {'data': 'test_data'}
    openapi_spec = OpenAPISpec(data=given_data)

    assert openapi_spec.data == given_data
    assert openapi_spec.created_at.date() == datetime.today().date()