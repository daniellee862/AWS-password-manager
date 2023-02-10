import boto3
import json
sm = boto3.client('secretsmanager')


def create_secret(secret_name, user_id, password):
    user_input_dict = {
        'user_id': user_id,
        'password': password
    }
    user_input_to_json = json.dumps(user_input_dict)

    try:
        sm.create_secret(
            Name=secret_name,
            SecretString=user_input_to_json
        )
    except Exception:
        return 'error'
    return 'success'


def list_secrets():
    secret_list = [secret['Name']
                   for secret in sm.list_secrets()['SecretList']]
    return secret_list


def retrieve_secret(secret):
    retrieved_secret = sm.get_secret_value(
        SecretId=secret)['SecretString']
    f = open('secrets_file.txt', 'a+')
    f.write(f'{secret} = {retrieved_secret}\n')


def delete_secret(secret):
    sm.delete_secret(SecretId=secret)
