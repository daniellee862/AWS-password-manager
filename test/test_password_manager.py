from src.functions import create_secret, list_secrets, retrieve_secret, delete_secret
from unittest.mock import patch
import json
import boto3
import pytest


# CREATE SECRET

@pytest.fixture
def sm_client():
    return boto3.client('secretsmanager')


def test_create_secret(sm_client, mocker):
    mock_create_secret = mocker.patch.object(sm_client, 'create_secret')
    secret_name = 'test_secret'
    user_id = 'test_user'
    password = 'test_password'
    result = create_secret(secret_name, user_id, password)

    mock_create_secret.assert_called_once_with(
        Name=secret_name,
        SecretString=json.dumps({'user_id': user_id, 'password': password})
    )
    assert result == 'success'
