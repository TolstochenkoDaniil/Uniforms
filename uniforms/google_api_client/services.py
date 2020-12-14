import pickle
import os.path

from googleapiclient import errors
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


creds_dir = os.path.join(os.path.dirname(__file__), 'creds')


def handle_http_errors(function):
    def wrapper(self, *args, **kwargs):
        try:
            return function(self, *args, **kwargs)
        except errors.HttpError as error:
            self.error = error
            
    return wrapper


class AppsScriptService:
    def __init__(self, service):
        self.service = service
        self._response = None
        self.error = None
        self.trace = None
    
    # @handle_http_errors   
    def execute_script(self, request: dict, script_id: str):
        response = self.service.scripts().run(
            body=request,
            scriptId=script_id
        ).execute()
        
        self._process_response(response)
    
    def _process_response(self, response):
        if 'error' in response:
            error = response['error']['details'][0]
            self.error = error
        
            if 'scriptStackTraceElements' in error:
                for trace in error['scriptStackTraceElements']:
                    self.trace = "\t{0}: {1}".format(trace['function'],trace['lineNumber'])
        
        self._response = response
            
    @property
    def response(self):
        return self._response


class ServiceProvider:
    SCOPES = [
        "https://www.googleapis.com/auth/forms",
        "https://www.googleapis.com/auth/forms.currentonly",
        "https://www.googleapis.com/auth/script.scriptapp",
        "https://www.googleapis.com/auth/script.external_request"
    ]
    
    def __init__(self, version='v1', port=8000):
        self.version = version
        self._port = port
        self._credentials = None
    
    def get_service(self) -> AppsScriptService:
        service =  build(
            'script',
            self.version,
            credentials=self.credentials
        )
        
        return AppsScriptService(service=service)
    
    @property
    def credentials(self):
        self._set_credentials()
        
        return self._credentials
        
    def _set_credentials(self):
        self._load_token()
    
    def _load_token(self):
        token_file = os.path.join(creds_dir,'token.pickle')
        
        if os.path.exists(token_file):
            with open(token_file,'rb') as token:
                self._credentials = pickle.load(token)
        
        self._validate_credentials()
        
    def _validate_credentials(self):
        if not self._credentials or not self._credentials.valid:
            if self._credentials and self._credentials.expired and self._credentials.refresh_token:
                self._credentials.refresh(Request())
            else:
                self._credentials = self._get_credentials_from_local_flow(port=self._port)
            
            self._dump_credentials()
    
    @classmethod
    def _get_credentials_from_local_flow(cls, port):
        flow = InstalledAppFlow.from_client_secrets_file(os.path.join(creds_dir,'credentials.json'), cls.SCOPES)
        credentials = flow.run_local_server(port=port)
        
        return credentials

    def _dump_credentials(self):
        with open(os.path.join(creds_dir,'token.pickle'), 'wb') as token:
            pickle.dump(self._credentials, token)