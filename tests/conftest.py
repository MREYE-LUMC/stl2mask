from __future__ import annotations

from pathlib import Path

import pytest
from click.testing import CliRunner


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


@pytest.fixture
def data_path(request: pytest.FixtureRequest) -> Path:
    return Path(request.config.rootpath) / "tests/_data"
