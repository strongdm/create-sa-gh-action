# Copied from: https://github.com/strongdm/accessbot/blob/main/plugins/sdm/lib/service/sdm_service.py
import strongdm
import os


def create_sdm_service(api_access_key, api_secret_key, log):
    client = strongdm.Client(
        api_access_key,
        api_secret_key,
        host=os.getenv("SERVER_HOST"),
        insecure=True
    )
    return SdmService(client, log)


class SdmService:
    def __init__(self, client, log):
        self.__client = client
        self.__log = log
    
    def create_account(self, name):
        """
        Creates a service account
        """
        try:
            self.__log.debug("##SDM## SdmService.create_account")
            account = strongdm.Service(name=name)
            response = self.__client.accounts.create(account)
        except Exception as ex:
            raise Exception("Create account failed: " + str(ex)) from ex
        return response.account, response.token
