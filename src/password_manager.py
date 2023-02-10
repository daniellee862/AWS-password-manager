from functions import create_secret, list_secrets, retrieve_secret, delete_secret
import boto3
sm = boto3.client('secretsmanager')

'''> Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:'''

# LOOP CONDITION FOR SECRET MANAGER APP
exit = False

while exit == False:

    user_input = input(
        '> Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:\n')

    if user_input == 'e':
        # CREATE SECRET FUNCTION
        secret_name = input('> Secret identifier: ')
        if " " in secret_name or type(secret_name) != str:
            print('Invalid input!')
            break
        user_id = input('> UserId: ')
        if " " in user_id:
            print('Invalid input!')
            break
        password = input('> Password: ')
        if " " in password:
            print('Invalid input!')
            break
        response = create_secret(secret_name, user_id, password)
        if response == 'error':
            print('Connection error, try again')
        else:
            print('Secret saved!')

    elif user_input == 'r':
        # RETRIEVE PARTICULAR SECRET
        secret_to_retrieve = input('> Specify secret to retrieve: ')
        retrieve_secret(secret_to_retrieve)
        print('> Secrets stored in local file secrets.txt')

    elif user_input == 'd':
        # DELETE SECRET
        secret_to_delete = input('> Specify secret to delete: ')
        delete_secret(secret_to_delete)
        print('> Deleted')

    elif user_input == 'l':
        # LIST ALL SECRETS NAMES FUNCTION
        secret_list = list_secrets()
        list_length = len(secret_list)
        if list_length == 0:
            print(list_length, 'secrets available.')
        else:
            print(list_length, 'secret(s) available.')
            for secret in secret_list:
                print(secret)

    elif user_input == 'x':
        exit = True
        print('Thank you. Goodbye.')
        break
