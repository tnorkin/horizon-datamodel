from enum import Enum
from .Dataset import Dataset


class StatusEnum(str, Enum):
    """The status of a data release within the curation process.

    created = "Created"
        Default status when a record is first created in the repository.
    deprecated = "Deprecated"
        Data release was previously published but access to the data files needed to be removed due to errors or sensitivity converns.
    locked = "Locked"
        Data release is not public but has been locked to edits to allow for an external review period.
    published = "Published"
        Data release has received Bureau approval and is publicly available.
    revised = "Revised"
        Data release has been revised.
    provisional = "Provisional"
        Data release is subject to revision and has been released prior to Bureau approval to meet an immediate need.
    submitted = "Submitted"
        Data release has been submitted to the curation team
    underRevision = "Under Revision"
        Data release is being revised. The dataset metadata may be available but files are not accessible.
    """

    created = "Created"
    deprecated = "Deprecated"
    locked = "Locked"
    provisional = "Provisional"
    published = "Published"
    revised = "Revised"
    submitted = "Submitted"
    underRevision = "Under Revision"


class UsgsReleaseTypeEnum(str, Enum):
    """The type of release. Different types of releases fall under different USGS policy requirements.

    dataRelease = "Data Release"
        Data that are released as a static dataset and governed by USGS Survey Manual Chapter 502.8
    dynamic = "Dynamic"
        Data that are continually collected, processed, quality-controlled, and released in real-time or near-real-time.
    legacy = "Legacy"
        Data that were released prior to the implementation of USGS Survey Manual Chapter 502.8.
    sensitive = "Sensitive"
        Data that, if made public, would result in an adverse effect on a taxon or a living individual or data that may have significant economic implications if disclosed prior to public release.
    softwareRelease = "Software Release"
        Software that were released prior to the requirement to publish software at code.usgs.gov.
    """

    dataRelease = "Data Release"
    dynamic = "Dynamic"
    legacy = "Legacy"
    softwareRelease = "Software Release"


class DataRelease(Dataset):
    """Class that extends Dataset to include properties necessary for curating data within a data repository.

    status: StatusEnum = "Created"
        The status of a data release within the curation process.
    usgsReleaseType: UsgsReleaseTypeEnum
        The type of release. Different types of releases fall under different USGS policy requirements.
    """

    status: StatusEnum = "Created"
    usgsReleaseType: UsgsReleaseTypeEnum = "Data Release"
