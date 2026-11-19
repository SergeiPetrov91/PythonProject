import pytest

[pytest]
addopts =
    --headed
    --browser chromium
    --browser firefox
    --screenshot only-on-failure
    --tracing retain-on-failure
