from __future__ import annotations

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        action="store",
        default="android",
        choices=["android", "ios"],
        help="Platform to run tests on: android or ios"
    )


def pytest_configure(config):
    """Register custom markers"""
    config.addinivalue_line(
        "markers", "android: mark test to run only on Android platform"
    )
    config.addinivalue_line(
        "markers", "ios: mark test to run only on iOS platform"
    )