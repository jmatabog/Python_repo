import json
import pickle
import os.path
from cryptography.fernet import Fernet
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


SCOPES = ['https://www.googleapis.com/auth/calendar']

CREDENTIALS_FILE = os.getcwd()+'/.config/sys/.credentials.json'


def get_pickle_dir(username):
    """
    This function creates a pickle file that will store the credentials
    of each user who uses this program
    """
    
    credentials = None

    pickle_path = os.getcwd()+'/.config/users/'+username+'/'+username+'.pickle'
    

    if os.path.exists(pickle_path):
        with open(pickle_path, 'rb') as pickle_file:
            credentials = pickle.load(pickle_file)

    if not credentials or not credentials.valid:
        
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
            
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            credentials = flow.run_local_server(port = 0)

    with open(pickle_path, 'wb') as token_file:
        pickle.dump(credentials, token_file)

    return pickle_path


def encrypt_user_password(password):
    
    """
    This function creates an encryption key and uses it to encrypt the 
    new user's password that is entered as a parameter.
    param: password
    return: the encrypted password and the decryption key
    """
    enc_key = Fernet.generate_key()

    encoded = password.encode()

    f = Fernet(enc_key)

    password_encrypted = f.encrypt(encoded)

    return password_encrypted, enc_key

    
def decrypt_user_password(decryption_key, encrypted_password):
    """
    This function decrypts the user's passsword, so that it may be
    used in verification of valid users.
    param: decryption_key, encrypted_password
    returns: the decrypted password
    """

    f = Fernet(decryption_key)

    decrypted_password = f.decrypt(encrypted_password)

    return decrypted_password

if __name__ == "__main__":
    a = get_pickle_dir('codingclinic')
    print(a)