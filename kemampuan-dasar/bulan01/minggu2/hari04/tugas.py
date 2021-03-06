from injector import Injector, Module, singleton, provider


class Api:
    def fetch_remote_data(self):
        print('Api called')
        return 42


class BusinessLogic:
    def __init__(self, api: Api):
        self.api = api

    def do_stuff(self):
        api_result = self.api.fetch_remote_data()
        print(f'the api returned a result: {api_result}')
        # do something with the data and return a result

# ---

if __name__ == '__main__':
    api = Api()
    logic = BusinessLogic(api=api)

    # ...
    print(logic.do_stuff())



class Api:
    def fetch_remote_data(self):
        print('Api called')
        return 42
class BusinessLogic:
    def __init__(self, api: Api):
        self.api = api

    def do_stuff(self):
        api_result = self.api.fetch_remote_data()
        print(f'the api returned a result: {api_result}')
        # do something with the data and return a result
# print(logic.do_stuff())



class AppModule(Module):
    @singleton
    @provider
    def provide_business_logic(self, api: Api) -> BusinessLogic:
        return BusinessLogic(api=api)

    @singleton
    @provider
    def pro_api(self) -> Api:
        # there is no complex logic in our case,
        # but you can use this method to hide the complexity of initial configuration
        # e.g. when instantiating a particular DB connector.
        return Api()

if __name__ == '__main__':
    injector = Injector(AppModule())

    logic = injector.get(BusinessLogic)
    logic.do_stuff()


class TestApi(Api):
    def fetch_remote_data(self):
        print('Demo Api called')
        return 24
class TestAppModule(Module):

    @singleton
    @provider
    def provide_api(self) -> Api:
        return TestApi()
if __name__ == '__main__':
    real_injector = Injector(AppModule())
    test_injector = Injector([AppModule(), TestAppModule()])

    real_logic = real_injector.get(BusinessLogic)
    real_logic.do_stuff()

    test_logic = test_injector.get(BusinessLogic)
    test_logic.do_stuff()
