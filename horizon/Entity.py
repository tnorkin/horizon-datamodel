from pydantic import BaseModel, HttpUrl
from typing import Optional
from enum import Enum
from datetime import datetime


class NameTypeEnum(str, Enum):
    """The type of entity described by a name

    Args:
        str (_type_): _description_
        Enum (_type_): _description_
    """

    usgs_personal = "USGS Personal"
    personal = "Personal"
    organizational = "Organizational"
    service = "Service"


class ContributorTypeEnum(str, Enum):
    """The type of contributor of the resource.

    Args:
        str (_type_): _description_
        Enum (_type_): _description_
    """

    ContactPerson = "Contact Person"
    DataCollector = "Data Collector"
    DataCurator = "Data Curator"
    DataManager = "Data Manager"
    Distributor = "Distributor"
    Editor = "Editor"
    HostingInstitution = "Hosting Institution"
    Producer = "Producer"
    ProjectLeader = "Project Leader"
    ProjectManager = "Project Manager"
    ProjectMember = "Project Member"
    RegistrationAgency = "Registration Agency"
    RegistrationAuthority = "Registration Authority"
    RelatedPerson = "Related Person"
    Researcher = "Researcher"
    ResearchGroup = "Research Group"
    RightsHolder = "Rights Holder"
    Sponsor = "Sponsor"
    Supervisor = "Supervisor"
    WorkPackageLeader = "Work Package Leader"
    Other = "Other"


class Entity(BaseModel):
    """Person, Organization, or Service related to a resource

    Fields
    ------
    entity_id: Optional[str]
        Identifier to uniquely identify an entity within a given system
    name: str
        Name by which an entity is known
    nameType: NameTypeEnum
        The type of entity described by a name
    nameIdentifier: Optional[str]
        A globally unique persistent identifier for an entity (e.g., ORCID iD, ROR ID).

    """

    entity_id: Optional[str]
    name: str
    nameType: NameTypeEnum
    nameIdentifier: Optional[str]
    email: Optional[str]


class Creator(Entity):
    """The entity responsible for producing the resource.

    Fields
    ------
    position: int
        Position that the creator appears within a citation
    affiliation: Optional[str]
        The organization with which a creator is affiliated
    affiliationIdentifier: Optional[str]
        A globally unique persistent identifier for the affiliated organization.
    """

    position: int
    affiliation: Optional[str]
    affiliationIdentifier: Optional[str]


class Contributor(Creator):
    """The institution or person responsible for collecting, managing, distributing,
    or otherwise contributing to the development of the resource.

    Fields
    ------
    contributorType: ContributorTypeEnum
        The type of contributor of the resource.
    """

    contributorType: ContributorTypeEnum
