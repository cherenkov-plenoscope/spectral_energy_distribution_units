def pytest_configure(config):
    config.addinivalue_line("markers", "nottravis: Travis does not test this.")
