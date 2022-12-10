from fastapi.middleware.cors import CORSMiddleware


class DefineConfiguration:
    @staticmethod
    def configureCors(app):
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"])
