from typing import ClassVar

from datamodel_code_generator.model.pydantic.base_model import BaseModel


class CustomRootType(BaseModel):
    TEMPLATE_FILE_PATH: ClassVar[str] = 'schematics/BaseModel.jinja2'
    BASE_CLASS: ClassVar[str] = 'schematics.BaseModel'