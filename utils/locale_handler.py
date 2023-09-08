class LocaleHandler:
    def __init__(self, locale: str):
        self.locale = locale


    @property
    def get_language(self):
        return self.locale    
