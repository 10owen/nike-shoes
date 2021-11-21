from pymemcache.client.base import Client
import os
class Memcached():
    client = None
    ip = ""
    port = ""
    def __init__(self):
        self.ip = os.getenv("MEMCACHED_IP")
        if self.ip is None:
            self.ip = "localhost"
        self.port = os.getenv("MEMCACHED_PORT")
        if self.port is None:
            self.port = "11211"
        self.client = Client((self.ip, self.port))

    def get(self, key):
        data = self.client.get(key)
        if data is None: return None
        return data.decode("utf-8")

    def set(self, key, value):
        return self.client.set(key, value)

if __name__ == "__main__":
    memcached = Memcached()
    memcached.set('test', 100)
    test_get = memcached.get('test')
    test_get = int(test_get)
    if test_get == 100:
        print("good!")