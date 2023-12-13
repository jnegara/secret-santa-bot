from configparser import ConfigParser


class EmailConfig:
    def __init__(self, cp: ConfigParser):
        ecp = cp['EMAIL']
        
        self.__email: str = ecp['email']
        self.__password: str = ecp['password']
        self.__hostname: str = ecp['hostname']
        self.__port: int = int(ecp['port'])
    
    def email(self) -> str:
        return self.__email

    def password(self) -> str:
        return self.__password
    
    def hostname(self) -> str:
        return self.__hostname
    
    def port(self) -> int:
        return self.__port


class Config:
    def __init__(self, config_file: str = 'config.ini'):
        cp = ConfigParser()
        cp.read(config_file)

        self.__email_config: EmailConfig = EmailConfig(cp)
    
    def email(self) -> EmailConfig:
        return self.__email_config


CONFIG: Config = Config()