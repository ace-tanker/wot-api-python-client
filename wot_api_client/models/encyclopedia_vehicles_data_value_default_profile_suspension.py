# coding: utf-8

"""
    World of Tanks

    OpenAPI specification for the Wargaming.net Public API. The official Wargaming.net Public API documentation can be found at the Wargaming [Developer's room](https://developers.wargaming.net/).

    The version of the OpenAPI document: 1.0.0
    Contact: contact@ace-tanker.net
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class EncyclopediaVehiclesDataValueDefaultProfileSuspension(BaseModel):
    """
    Suspension characteristics
    """ # noqa: E501
    tier: StrictInt = Field(description="Tier")
    name: StrictStr = Field(description="Module name")
    weight: StrictInt = Field(description="Weight (kg)")
    tag: StrictStr = Field(description="Module tag")
    load_limit: StrictInt = Field(description="Load limit (kg)")
    traverse_speed: StrictInt = Field(description="Traverse speed (deg/s)")
    steering_lock_angle: StrictInt = Field(description="Maximum wheel turning angle (for wheeled vehicles)")
    __properties: ClassVar[List[str]] = ["tier", "name", "weight", "tag", "load_limit", "traverse_speed", "steering_lock_angle"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of EncyclopediaVehiclesDataValueDefaultProfileSuspension from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EncyclopediaVehiclesDataValueDefaultProfileSuspension from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tier": obj.get("tier"),
            "name": obj.get("name"),
            "weight": obj.get("weight"),
            "tag": obj.get("tag"),
            "load_limit": obj.get("load_limit"),
            "traverse_speed": obj.get("traverse_speed"),
            "steering_lock_angle": obj.get("steering_lock_angle")
        })
        return _obj


