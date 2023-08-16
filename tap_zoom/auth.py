""""""
from __future__ import annotations

from singer_sdk.authenticators import OAuthAuthenticator, SingletonMeta

AUTH_URL = "https://zoom.us/oauth/token"


class ZoomOAuthAuthenticator(OAuthAuthenticator, metaclass=SingletonMeta):
    @property
    def auth_endpoint(self) -> str:
        return self.config.get("auth_url", AUTH_URL)

    @property
    def oauth_request_body(self) -> dict:
        """Get formatted body of the OAuth authorization request."""

        return {
            "grant_type": "authorization_code",
            "account_id": self.config.get("account_id"),
            "grant_type": "authorization_code",
            "code": self.config.get("code"),
            "redirect_uri": self.config.get("redirect_uri"),
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
