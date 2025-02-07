from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from enum import Enum
from datetime import datetime
from .CatalogedResource import CatalogedResource
from .Entity import Entity, Creator, Contributor
from .License import License
from .Distribution import Distribution
from .Location import Location


class Keyword(BaseModel):
    """A keyword or tag describing the resource.
    concept: str
        The keyword or tag
    conceptScheme: str = None
        The name of the scheme or classification code or authority (e.g., USGS Thesaurus)
    conceptUri: Optional[HttpUrl]
        The URI of the concept
    """

    concept: str
    conceptScheme: str = None
    conceptUri: Optional[HttpUrl]


class DataciteRelationTypeEnum(str, Enum):
    """Description of the relationship of the resource being described and the related resource."""

    IsCitedBy = "Is Cited By"
    Cites = "Cites"
    IsSupplementTo = "Is Supplement To"
    IsSupplementedBy = "Is Supplemented By"
    IsContinuedBy = "Is Continued By"
    Continues = "Continues"
    IsNewVersionOf = "Is New Version Of"
    IsPreviousVersionOf = "Is Previous Version Of"
    IsPartOf = "Is Part Of"
    HasPart = "Has Part"
    IsReferencedBy = "Is Referenced By"
    References = "References"
    IsDocumentedBy = "Is Documented By"
    Documents = "Documents"
    IsCompiledBy = "Is Compiled By"
    Compiles = "Compiles"
    IsVariantFormOf = "Is Variant Form Of"
    IsOriginalFormOf = "Is Original Form Of"
    IsIdenticalTo = "Is Identical To"
    HasMetadata = "Has Metadata"
    IsMetadataFor = "Is Metadata For"
    Reviews = "Reviews"
    IsReviewedBy = "Is Reviewed By"
    IsDerivedFrom = "Is Derived From"
    IsSourceOf = "Is Source Of"
    Describes = "Describes"
    IsDescribedBy = "Is Described By"
    HasVersion = "Has Version"
    IsVersionOf = "Is Version Of"
    Requires = "Requires"
    IsRequiredBy = "Is Required By"
    Obsoletes = "Obsoletes"
    IsObsoletedBy = "Is Obsoleted By"
    IsPublishedIn = "Is Published In"


class RelatedIdentifierTypeEnum(str, Enum):
    """The type of related identifier."""

    ARK = "ARK"
    arXiv = "arXiv"
    bibcode = "bibcode"
    DOI = "DOI"
    EAN13 = "EAN13"
    EISSN = "EISSN"
    Handle = "Handle"
    IGSN = "IGSN"
    ISBN = "ISBN"
    ISSN = "ISSN"
    ISTC = "ISTC"
    LISSN = "LISSN"
    LSID = "LSID"
    PMID = "PMID"
    PURL = "PURL"
    UPC = "UPC"
    URL = "URL"
    URN = "URN"
    w3id = "w3id"


class RelatedIdentifier(BaseModel):
    """Identifier of related resource.

    Fields
    ------
    dataciteRelationType: DataciteRelationTypeEnum
        Description of the relationship of the resource being described and the related resource.
    relatedIdentifier: str
        The identifier of the related resource.
    primaryRelatedIdentifier: bool
        An indication if the related resource was developed alongside the cataloged resource and thus critical to the complete understanding of the cataloged resource.
    relatedIdentifierType: RelatedIdentifierTypeEnum
        The type of related identifier.
    """

    dataciteRelationType: DataciteRelationTypeEnum
    relatedIdentifier: str
    primaryRelatedIdentifier: bool  # Should we get rid of this?
    relatedIdentifierType: RelatedIdentifierTypeEnum


class AlternateIdentifierTypeEnum(str, Enum):
    """The type of alternate identifier

    "ARK", "Servcat Number", "Genbank Accession Number",
    "IGSN", "LSID", "PURL", "Ref Seq ID", "Local Identifier", "Metadata Identifier"
    """

    ARK = "ARK"
    ServcatNumber = "Servcat Number"
    GenbankAccessionNumber = "Genbank Accession Number"
    IGSN = "IGSN"
    LSID = "LSID"
    PURL = "PURL"
    RefSeqID = "Ref Seq ID"
    LocalIdentifier = "Local Identifier"
    MetadataIdentifier = "Metadata Identifier"


class AlternateIdentifier(BaseModel):
    """An identifier or identifiers other than the primary Identifier applied to the resource being registered.

    Fields
    ------
    identifier: str
        An identifier or identifiers other than the primary Identifier applied to the resource being registered.
    identifierType: AlternateIdentifierTypeEnum
        The type of alternate identifier
    """

    identifier: str
    identifierType: AlternateIdentifierTypeEnum


class PeriodOfTime(BaseModel):
    """An interval of time that is named or defined by its start and end dates.

    The interval can be open. For example, it can have just a start or just an end.

    Fields
    ------
    startDate: Optional[datetime]
        The start of the period.
    endDate: Optional[datetime]
        The end of the period
    """

    startDate: Optional[datetime]
    endDate: Optional[datetime]


class UsgsDataSource(BaseModel):
    """The USGS Science Center or Program responsible for managing the resource.

    The name and dataSourceId should come from Gluebucket.
    name: str
    dataSourceId: str
    """

    name: str
    dataSourceId: str


class UsgsMissionArea(BaseModel):
    """The USGS Mission Area responsible for managing the resource.

    The Mission Area name and ID should come from Gluebucket service.
    name: str
    missionAreaId: str
    """

    name: str
    missionAreaId: str


class VersionHistory(BaseModel):
    """Description of versions of the dataset described within a given identifier.


    version: Optional[str]
        The version indicator (name or identifier) of a resource.
    issued: Optional[datetime]
        Date of formal issuance (e.g., publication) of the resource.
    versionNotes: Optional[datetime]
        A description of changes between this version and the previous version of the resource
    """

    version: Optional[str]
    issued: Optional[datetime]
    versionNotes: Optional[datetime]


class Component(BaseModel):
    """A subset of a Dataset that may require additional
    descriptive metadata to be discovered and understood by
    users of the data.

    Fields
    ------
    identifier: Optional[HttpUrl]
        A granular DOI used to identify the component that is different that the
        CatalogedResource's DOI
    title: str
        Name given to the component
    description: str
        Free-text description of the component
    usgsCitation: str
        The recommended citation for the component.
        In most cases this citation will be the same as the Dataset citation
    catalogRecord: bool
        Boolean indication if the metadata should be cataloged independently from the Dataset
    distribution: List[Distribution]
        An available distribution of the component.
    alternateIdentifier: Optional[AlternateIdentifier]
        USGS Metadata PID
    """

    identifier: Optional[HttpUrl]
    title: str
    description: str
    usgsCitation: str
    catalogRecord: bool
    distribution: List[Distribution]
    alternateIdentifier: Optional[AlternateIdentifier]


class Dataset(CatalogedResource):
    """A collection of data, published or curated by a single agent, and available for access or download in one or more representations.

    Fields
    ------
    issued: datetime
        Date of formal issuance (e.g., publication) of the resource.
    modified: Optional[datetime]
        Most recent date on which the resource was changed, updated or modified.
    creator: Creator
        The entity responsible for producing the resource.
    publisher: Entity
        The entity responsible for making the resource available.
    usgsCitation: str
        The recommended citation for the resource.
    contactPoint: Entity
        Relevant contact information for the cataloged resource.
    usgsMetadataContactPoint: Entity
        The entity responsible for creating and maintaining the metadata for the resource.
    license: License
        A legal document under which the resource is made available.
    usgsDataSource: UsgsDataSource
        The USGS Science Center or Program responsible for managing the resource.
    distribution: List[Distribution]
        An available distribution of the dataset.
    component: List[Component]
        A container for holding components or subsets of the overall Dataset
        that require additional metadata to be discovered and understood
    keyword: Optional[List[Keyword]]
        A keyword or tag describing the resource.
    spatial: Optional[Location]
        The geographical area covered by the dataset.
    temporal: Optional[List[PeriodOfTime]]
        The temporal period that the dataset covers.
    relation: Optional[List[RelatedIdentifier]]
        A resource with a relationship to the cataloged resource.
        This property includes DCAT sub-properties hasPart, isReferencedBy, previousVersion, replaces.
    alternateIdentifier: Optional[List[AlternateIdentifier]]
        An identifier or identifiers other than the primary Identifier applied to the resource being registered.
    usgsPurpose: Optional[str]
        A summary of the intentions with which the resource was developed
    usgsMissionArea: Optional[UsgsMissionArea]
        The USGS Mission Area responsible for managing the resource.
    qualifiedAttribution: Optional[Contributor]
        Link to an Agent having some form of responsibility for the resource
    versionHistory: Optional[VersionHistory]
        Description of versions of the dataset described within a given identifier.
    """

    issued: datetime
    modified: Optional[
        datetime
    ]  # Adding this here instead of under version as an optional field.
    creator: List[Creator]
    publisher: Entity
    usgsCitation: str
    contactPoint: Entity
    usgsMetadataContactPoint: Entity
    license: License
    usgsDataSource: UsgsDataSource
    distribution: List[Distribution]
    component: List[Component]
    keyword: Optional[List[Keyword]]
    spatial: Optional[Location]
    temporal: Optional[
        List[PeriodOfTime]
    ]  # I'm not sure if this can actually be a list in DCAT
    relation: Optional[List[RelatedIdentifier]]
    alternateIdentifier: Optional[List[AlternateIdentifier]]
    usgsPurpose: Optional[str]
    usgsMissionArea: Optional[UsgsMissionArea]
    qualifiedAttribution: Optional[Contributor]
    versionHistory: Optional[VersionHistory]
