from urllib import response
import requests
import getpass

def main():

    url = 'https://api.github.com/user'

    # Input username and password
    # username = input("Username: ")
    # password = getpass.getpass("Password:")
    token = getpass.getpass("Token: ")

    # # Process

    # Using username and password (401 error)
    # response = requests.get(
    #     url, 
    #     auth=(username, password)
    # )

    # Using token
    headers = {'Authorization': 'token ' + token}
    response = requests.get(url, headers=headers)

    # Result
    print(response)
    print('\n' + response.text)


if __name__ == '__main__':
    main()