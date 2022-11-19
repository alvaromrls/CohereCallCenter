class connexion:
    server_url = "/api"
    endpoint = {"metadata": "/metadata", "failed_messages": "/errors"}
    PORT = 5000
    URL = "http://localhost"

    def get_url(self, endpoint):
        server_endpoint = self.endpoint.get(endpoint)
        if server_endpoint:
            return self.server_url + server_endpoint
        else:
            return server_endpoint

    def get_port(self):
        return self.PORT

    def connexion_string(self):
        return f"{self.URL}:{self.PORT}"


def __init__():
    pass
