from __future__ import annotations

from pathlib import Path

import pytest

from stl2mask.helpers import full_suffix, with_suffix


@pytest.mark.parametrize(
    "path, expected",
    [
        (Path("file.nii"), ".nii"),
        (Path("file.nii.gz"), ".nii.gz"),
        (Path("file.nii.gz.zip"), ".nii.gz.zip"),
        (Path("archive.tar.gz"), ".tar.gz"),
        (Path("document.txt"), ".txt"),
        (Path("no_extension"), ""),
    ],
)
def test_full_suffix(path: Path, expected: str) -> None:
    assert full_suffix(path) == expected


@pytest.mark.parametrize(
    "path, suffix, expected",
    [
        (Path("file"), ".nii", Path("file.nii")),
        (Path("file.nii"), ".stl", Path("file.stl")),
        (Path("file.nii.gz"), ".stl", Path("file.stl")),
        (Path("file.stl"), ".nii.gz", Path("file.nii.gz")),
        (Path("file.stl.zip"), ".nii.gz", Path("file.nii.gz")),
    ],
)
def test_with_suffix(path: Path, suffix: str, expected: Path) -> None:
    assert with_suffix(path, suffix) == expected
