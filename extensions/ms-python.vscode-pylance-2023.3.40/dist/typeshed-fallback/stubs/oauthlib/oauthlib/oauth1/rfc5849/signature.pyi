from _typeshed import Incomplete
from typing import Any

log: Any

def signature_base_string(http_method: str, base_str_uri: str, normalized_encoded_request_parameters: str) -> str: ...
def base_string_uri(uri: str, host: str | None = ...) -> str: ...
def collect_parameters(
    uri_query: str = ...,
    body: Incomplete | None = ...,
    headers: Incomplete | None = ...,
    exclude_oauth_signature: bool = ...,
    with_realm: bool = ...,
): ...
def normalize_parameters(params) -> str: ...
def sign_hmac_sha1_with_client(sig_base_str, client): ...
def verify_hmac_sha1(request, client_secret: Incomplete | None = ..., resource_owner_secret: Incomplete | None = ...): ...
def sign_hmac_sha1(base_string, client_secret, resource_owner_secret): ...
def sign_hmac_sha256_with_client(sig_base_str, client): ...
def verify_hmac_sha256(request, client_secret: Incomplete | None = ..., resource_owner_secret: Incomplete | None = ...): ...
def sign_hmac_sha256(base_string, client_secret, resource_owner_secret): ...
def sign_hmac_sha512_with_client(sig_base_str: str, client): ...
def verify_hmac_sha512(request, client_secret: str | None = ..., resource_owner_secret: str | None = ...): ...
def sign_rsa_sha1_with_client(sig_base_str, client): ...
def verify_rsa_sha1(request, rsa_public_key: str): ...
def sign_rsa_sha1(base_string, rsa_private_key): ...
def sign_rsa_sha256_with_client(sig_base_str: str, client): ...
def verify_rsa_sha256(request, rsa_public_key: str): ...
def sign_rsa_sha512_with_client(sig_base_str: str, client): ...
def verify_rsa_sha512(request, rsa_public_key: str): ...
def sign_plaintext_with_client(_signature_base_string, client): ...
def sign_plaintext(client_secret, resource_owner_secret): ...
def verify_plaintext(request, client_secret: Incomplete | None = ..., resource_owner_secret: Incomplete | None = ...): ...
