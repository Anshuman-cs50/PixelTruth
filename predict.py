"""Simple CLI and library wrapper for running image predictions.

This module provides a thin wrapper around `inference` utilities so
the codebase (and any callers) can request a label/confidence for an
image file path. The library function does not call `sys.exit()` so it
is safe to call from tests; the CLI entrypoint emits a non-zero exit
code on failure.
"""
from __future__ import annotations

import os
import sys
from typing import Tuple, Optional

from preprocessing import preprocess_image_bytes
from inference import load_model_safe, predict_image as _predict_image
from model_utils import get_model_path, get_model_url, get_model_sha256
from exceptions import PreprocessingError, ModelExecutionError


def predict_from_path(model, image_path: str) -> Tuple[Optional[str], Optional[float], Optional[object]]:
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    with open(image_path, "rb") as fh:
        image_bytes = fh.read()

    # reuse the shared cached preprocessing for uploaded files
    image = preprocess_image_bytes(image_bytes)
    return _predict_image(model, image)


def load_model_for_cli():
    return load_model_safe(
        model_path=get_model_path(), model_url=get_model_url(), model_sha256=get_model_sha256(), download_if_missing=True
    )


def main(argv: list[str] | None = None) -> int:
    argv = list(argv or sys.argv)
    if len(argv) < 2:
        print("Usage: python -m predict <image_path>")
        return 2

    image_path = argv[1]

    try:
        model = load_model_for_cli()
        label, confidence, _ = predict_from_path(model, image_path)
        if label is None:
            print("No model available; prediction could not be performed.")
            return 3
        print(f"Label: {label}")
        print(f"Confidence: {confidence:.4f}")
        return 0
    except (PreprocessingError, ModelExecutionError) as exc:
        print(f"Error: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
