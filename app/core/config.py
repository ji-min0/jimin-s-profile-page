from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    EMAIL_PROVIDER: str = "gmail" # 기본값 세팅 .env값으로 덮어씌워짐

    EMAIL_USER: str
    EMAIL_PASS: str

    CONTACT_EMAIL: str = "k.jimin2002@gmail.com" # 수정 여기도 .env값으로 덮어씌워짐

    EMAIL_HOST: str = ""
    EMAIL_PORT: int = 587 # 여긴 지금 gmail 디폴트라서 이 값인거임. 어차피 __init__ 함수에서 이메일에 맞게 강제할거임

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    def __init__(self, **values):
        super().__init__(**values)
        if self.EMAIL_PROVIDER == "naver":
            self.EMAIL_HOST = "smtp.naver.com"
            self.EMAIL_PORT = 465 # 여기 수정함
        elif self.EMAIL_PROVIDER == "gmail":
            self.EMAIL_HOST = "smtp.gmail.com"
            self.EMAIL_PORT = 587
        else:
            raise ValueError(
                "지원하지 않는 메일 서비스입니다. (naver/gmail만 사용 가능)"
            )


settings = Settings()
