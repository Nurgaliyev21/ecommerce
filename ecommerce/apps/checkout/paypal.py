import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "ARmBl8QMutuZjYK581CQVl7_t5IgQnkKIevFyLnigz-c5LyeptjDhYEzPREnHEWGf8Hr_Ss53GhVRNGt"
        self.client_secret = "EHaIcahrBoBJ61_sAnomkhcwXiaTE_4xVwmnSJ5roEc11f7OSz6O5h1tJPbG1OE44Xei9XfB8EB_8zgC"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
