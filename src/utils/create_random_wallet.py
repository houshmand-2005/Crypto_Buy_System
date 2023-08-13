import base64
import random
import string


def create_wallet_crypto():
    """Generate a random wallet address using Base64 encoding."""
    random_string = "".join(
        random.SystemRandom().choice(string.ascii_letters + string.digits)
        for _ in range(16)
    )
    random_bytes = random_string.encode("utf-8")
    wallet_address = base64.urlsafe_b64encode(random_bytes).decode("utf-8")
    return wallet_address
