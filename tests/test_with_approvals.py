import json
from pathlib import Path

import pytest
from approvaltests.approvals import verify
from refact.statement import statement


def test_with_approvals(all_statements):
    verify(all_statements)


@pytest.fixture
def all_statements(plays, invoices):
    result = ""
    for i, invoice in enumerate(invoices):
        result += f"--------- {i} ----------\n"
        result += statement(invoice, plays)
        result += "\n"
    return result


@pytest.fixture()
def plays(get_json_from_file) -> dict:
    return get_json_from_file("data/plays.json")


@pytest.fixture()
def invoices(get_json_from_file) -> dict:
    return get_json_from_file("data/invoices.json")


@pytest.fixture()
def get_json_from_file(get_file):
    def jsonify_file(filepath: str):
        return json.loads(get_file(filepath))

    return jsonify_file


@pytest.fixture()
def get_file():
    def read_file(file_path: str) -> str:
        return (Path(__file__).parent / file_path).read_text()

    return read_file
