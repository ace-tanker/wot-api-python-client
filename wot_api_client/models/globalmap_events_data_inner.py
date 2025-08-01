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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wot_api_client.models.globalmap_events_data_inner_fronts_inner import GlobalmapEventsDataInnerFrontsInner
from typing import Optional, Set
from typing_extensions import Self

class GlobalmapEventsDataInner(BaseModel):
    """
    GlobalmapEventsDataInner
    """ # noqa: E501
    event_id: StrictStr = Field(description="Event ID")
    event_name: StrictStr = Field(description="Event name")
    start: StrictStr = Field(description="Start time")
    end: StrictStr = Field(description="Finishing time")
    status: StrictStr = Field(description="Status")
    fronts: Optional[List[Optional[GlobalmapEventsDataInnerFrontsInner]]] = Field(description="Fronts. Only event fronts are presented in response.")
    __properties: ClassVar[List[str]] = ["event_id", "event_name", "start", "end", "status", "fronts"]

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
        """Create an instance of GlobalmapEventsDataInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in fronts (list)
        _items = []
        if self.fronts:
            for _item_fronts in self.fronts:
                if _item_fronts:
                    _items.append(_item_fronts.to_dict())
            _dict['fronts'] = _items
        # set to None if fronts (nullable) is None
        # and model_fields_set contains the field
        if self.fronts is None and "fronts" in self.model_fields_set:
            _dict['fronts'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GlobalmapEventsDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "event_id": obj.get("event_id"),
            "event_name": obj.get("event_name"),
            "start": obj.get("start"),
            "end": obj.get("end"),
            "status": obj.get("status"),
            "fronts": [GlobalmapEventsDataInnerFrontsInner.from_dict(_item) for _item in obj["fronts"]] if obj.get("fronts") is not None else None
        })
        return _obj


