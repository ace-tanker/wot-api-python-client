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
from typing import Any, ClassVar, Dict, List, Optional
from wot_api_client.models.encyclopedia_personalmissions_data_value_operations_value import EncyclopediaPersonalmissionsDataValueOperationsValue
from typing import Optional, Set
from typing_extensions import Self

class EncyclopediaPersonalmissionsDataValue(BaseModel):
    """
    EncyclopediaPersonalmissionsDataValue
    """ # noqa: E501
    campaign_id: StrictInt = Field(description="Campaign ID")
    name: StrictStr = Field(description="Campaign name")
    description: StrictStr = Field(description="Campaign description")
    operations: Optional[Dict[str, Optional[EncyclopediaPersonalmissionsDataValueOperationsValue]]] = Field(description="Campaign operations")
    __properties: ClassVar[List[str]] = ["campaign_id", "name", "description", "operations"]

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
        """Create an instance of EncyclopediaPersonalmissionsDataValue from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in operations (dict)
        _field_dict = {}
        if self.operations:
            for _key_operations in self.operations:
                if self.operations[_key_operations]:
                    _field_dict[_key_operations] = self.operations[_key_operations].to_dict()
            _dict['operations'] = _field_dict
        # set to None if operations (nullable) is None
        # and model_fields_set contains the field
        if self.operations is None and "operations" in self.model_fields_set:
            _dict['operations'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EncyclopediaPersonalmissionsDataValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "campaign_id": obj.get("campaign_id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "operations": dict(
                (_k, EncyclopediaPersonalmissionsDataValueOperationsValue.from_dict(_v))
                for _k, _v in obj["operations"].items()
            )
            if obj.get("operations") is not None
            else None
        })
        return _obj


