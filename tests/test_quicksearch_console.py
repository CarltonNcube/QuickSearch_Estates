#!/usr/bin/python3

from unittest.mock import patch
from io import StringIO
import pytest
from backend.console import QuickSearchConsole

# Mocking the SQLAlchemy session for testing
@patch("console.db_session")
def test_create(mock_db_session):
    console = QuickSearchConsole()
    mock_db_session.add.return_value = None
    mock_db_session.commit.return_value = None
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("create User")
    assert output.getvalue() == "New User created with ID: None\n"

@patch("console.db_session")
def test_show(mock_db_session):
    console = QuickSearchConsole()
    instance = "Test User"
    mock_db_session.query.return_value.filter_by.return_value.first.return_value = instance
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("show User 1")
    assert output.getvalue() == instance + "\n"

@patch("console.db_session")
def test_all(mock_db_session):
    console = QuickSearchConsole()
    instances = ["User 1", "User 2", "User 3"]
    mock_db_session.query.return_value.all.return_value = instances
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("all User")
    assert output.getvalue() == str(instances) + "\n"

@patch("console.db_session")
def test_destroy(mock_db_session):
    console = QuickSearchConsole()
    instance = "User 1"
    mock_db_session.query.return_value.filter_by.return_value.first.return_value = instance
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("destroy User 1")
    assert output.getvalue() == "User instance 1 deleted successfully\n"

@patch("console.db_session")
def test_update(mock_db_session):
    console = QuickSearchConsole()
    instance = "User 1"
    mock_db_session.query.return_value.filter_by.return_value.first.return_value = instance
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("update User 1 name John")
    assert output.getvalue() == "name updated successfully for User instance 1\n"

@patch("console.db_session")
def test_invalid_class_name(mock_db_session):
    console = QuickSearchConsole()
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("create InvalidClass")
    assert "*** Unknown class name ***" in output.getvalue()

@patch("console.db_session")
def test_emptyline(mock_db_session):
    console = QuickSearchConsole()
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("")  # Enter an empty line
    assert output.getvalue() == ""

@patch("console.db_session")
def test_quit(mock_db_session):
    console = QuickSearchConsole()
    assert console.do_quit("")  # Simulate quitting the console

@patch("console.db_session")
def test_EOF(mock_db_session):
    console = QuickSearchConsole()
    assert console.do_EOF("")  # Simulate reaching end of file (Ctrl+D)

@patch("console.db_session")
def test_default_invalid_syntax(mock_db_session):
    console = QuickSearchConsole()
    output = StringIO()
    with patch('sys.stdout', output):
        console.default("invalid_syntax")
    assert "*** Unknown syntax: missing command ***" in output.getvalue()

@patch("console.db_session")
def test_default_invalid_class_name(mock_db_session):
    console = QuickSearchConsole()
    output = StringIO()
    with patch('sys.stdout', output):
        console.default("InvalidClass")
    assert "*** Unknown syntax: invalid class name ***" in output.getvalue()

@patch("console.db_session")
def test_default_invalid_command(mock_db_session):
    console = QuickSearchConsole()
    output = StringIO()
    with patch('sys.stdout', output):
        console.default("User invalid_command")
    assert "*** Unknown syntax: invalid command ***" in output.getvalue()

# Additional test cases
@patch("console.db_session")
def test_invalid_instance_id(mock_db_session):
    console = QuickSearchConsole()
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("show User")
    assert "*** Usage: show <class name> <instance id> ***" in output.getvalue()

@patch("console.db_session")
def test_update_no_value(mock_db_session):
    console = QuickSearchConsole()
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("update User 1 name")
    assert "*** Usage: update <class name> <instance id> <attribute> <value> ***" in output.getvalue()

@patch("console.db_session")
def test_invalid_update(mock_db_session):
    console = QuickSearchConsole()
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("update User 1 invalid_attribute value")
    assert "*** Unknown syntax: invalid command ***" in output.getvalue()

@patch("console.db_session")
def test_invalid_destroy(mock_db_session):
    console = QuickSearchConsole()
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("destroy User")
    assert "*** Usage: destroy <class name> <instance id> ***" in output.getvalue()

@patch("console.db_session")
def test_invalid_show(mock_db_session):
    console = QuickSearchConsole()
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("show")
    assert "*** Usage: show <class name> <instance id> ***" in output.getvalue()

@patch("console.db_session")
def test_invalid_all(mock_db_session):
    console = QuickSearchConsole()
    output = StringIO()
    with patch('sys.stdout', output):
        console.onecmd("all")
    assert "*** Unknown class name ***" in output.getvalue()

if __name__ == "__main__":
    pytest.main()
