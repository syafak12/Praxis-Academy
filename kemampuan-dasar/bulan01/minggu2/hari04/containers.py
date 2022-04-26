# class EmailReader(object):
#     def __init__(self, client):
#         try:
#             self._client = client
#         except Exception as e:
#             raise e

#     def read(self):
#         # Implement function here
#         pass

from dependency_injector import providers, containers
from email_client import EmailClient
from email_reader import EmailReader

class Configs(containers.DeclarativeContainer):
    config = providers.Configuration('config')
    # other configs
    
class Clients(containers.DeclarativeContainer):
    email_client = providers.Singleton (EmailClient, Configs.config)
    # other clients
    
class Readers(containers.DeclarativeContainer):
    email_reader = providers.Factory(EmailReader, client=Clients.email_client)
    # other readers