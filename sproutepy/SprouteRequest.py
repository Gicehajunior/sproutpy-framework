class SproutRequest:
    def __init__(self, method, path, body=None):
        self.method = method
        self.path = path
        self.body = body if body else {}

    def handle_request(self, router):
        return router.route_request(self.path, self.method, self.body)