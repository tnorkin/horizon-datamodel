from pydantic import BaseModel, HttpUrl
from typing import Optional


class License(BaseModel):
    """A legal document under which the resource is made available.

    licenseIdentifier: Optional[str]
        A short, standardized version of the license name.
    license: str
        The full version of the license name or free text description of the license or rights associated with the resource.
    licenseUri: Optional[str]
        The URI of the license.
    licenseIdentifierScheme: Optional[str]
        The name of the license identifier scheme
    schemeUri: Optional[str]
        The URI of the licenseIdentifierScheme
    """

    licenseIdentifier: Optional[str]
    license: str
    licenseUri: Optional[HttpUrl]
    licenseIdentifierScheme: Optional[str]
    schemeUri: Optional[HttpUrl]
