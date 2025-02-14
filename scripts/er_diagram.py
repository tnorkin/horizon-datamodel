import erdantic as erd
import os
from pathlib import Path

cpath = Path.cwd().parents[0]
npath = Path.joinpath(cpath, "datamodel/horizon/")
os.chdir(npath)

from horizon.CatalogedResource import CatalogedResource
from horizon.Entity import Entity
from horizon.DataRelease import DataRelease
from horizon.License import License
from horizon.Location import Location
from horizon.Distribution import Distribution
from horizon.Dataset import Dataset

os.chdir(Path.cwd())

erd.draw(Entity, out="../diagrams/Entity-diagram.png")
erd.draw(License, out="../diagrams/License-diagram.png")
erd.draw(Location, out="../diagrams/Location-diagram.png")
erd.draw(Dataset, out="../diagrams/Dataset-diagram.png")
erd.draw(DataRelease, out="../diagrams/DataRelease-diagram.png")
erd.draw(CatalogedResource, out="../diagrams/CatalogedResource-diagram.png")
erd.draw(Distribution, out="../diagrams/Distribution-diagram.png")