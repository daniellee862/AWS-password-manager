
# 🚀 AWS-Powered Password Manager 🚀

![Python](https://img.shields.io/badge/Python-3.9%2B-blueviolet)

![Boto3](https://img.shields.io/badge/Boto3-1.17.0-blue)

![AWS](https://img.shields.io/badge/AWS-Secrets%20Manager-orange)

Welcome to the AWS-Powered Password Manager, a command-line application to securely store and retrieve your passwords using AWS Secrets Manager. Say goodbye to forgetting passwords and hello to convenience and security! 😎

## Getting Started

Before you dive into managing your passwords like a pro, make sure you have the following prerequisites in place:

-  Python 3.9 or above installed on your system.
-  Boto3 library version 1.17.0 or above.
-  AWS account credentials with Access Key ID and Secret Key.

## Installation 🛠️

To get started, follow these simple steps:

1. Clone this repository to your local machine.
2. Install the required libraries using pip:

   ```bash
   pip install boto3
   ```

## Usage 💻

In your terminal, navigate to the project directory and run the password_manager.py script :


   ```bash
   $ python password_manager.py
   ```

You'll be prompted to choose an action from the following options:

-  [e]ntry: Store a new secret.
-  [r]etrieval: Retrieve a secret and store it in a file.
-  [d]eletion: Delete a secret.
-  [l]isting: List all the stored secrets.
- e[x]it: Exit the password manager.


## Example workflow 🔄

```bash
> Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, or e[x]it:

> Secret identifier: 
Fortnite_Password 
> UserId:
username123
> Password:
P@ssw0rd!
> Secret saved.

> Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, or e[x]it:
l
> 1 secret(s) available
Fortnite_Password 

> Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, or e[x]it:
r
> Specify secret to retrieve:
Fortnite_Password 
> Secrets stored in local file secrets.txt

> Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, or e[x]it:
d
> Specify secret to delete:
Fortnite_Password 
> Deleted

> Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting, or e[x]it:
x
> Thank you. Goodbye.
```

## Testing 🧪 

To ensure the functionality of the password manager, thorough testing is performed using the pytest framework and the unittest.mock module. The src/functions.py module contains the core functions used for interaction with AWS Secrets Manager.

```python

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
```
