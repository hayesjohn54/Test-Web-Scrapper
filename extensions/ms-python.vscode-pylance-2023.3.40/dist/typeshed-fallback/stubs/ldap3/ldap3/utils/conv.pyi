from _typeshed import Incomplete

def to_unicode(obj: float | bytes | str, encoding: str | None = ..., from_server: bool = ...) -> str: ...
def to_raw(obj, encoding: str = ...): ...
def escape_filter_chars(text: float | bytes | str, encoding: str | None = ...) -> str: ...
def unescape_filter_chars(text, encoding: Incomplete | None = ...): ...
def escape_bytes(bytes_value: str | bytes) -> str: ...
def prepare_for_stream(value): ...
def json_encode_b64(obj): ...
def check_json_dict(json_dict) -> None: ...
def json_hook(obj): ...
def format_json(obj, iso_format: bool = ...): ...
def is_filter_escaped(text): ...
def ldap_escape_to_bytes(text): ...
