from __future__ import annotations

import os

import pytest
from supabase import Client, create_client


@pytest.fixture(scope="session")
def supabase() -> Client:
    url = os.environ.get("SUPABASE_TEST_URL")
    key = os.environ.get("SUPABASE_TEST_KEY")
    if not url or not key:
        raise ValueError("SUPABASE_TEST_URL and SUPABASE_TEST_KEY must be set")
    supabase: Client = create_client(url, key)
    return supabase
