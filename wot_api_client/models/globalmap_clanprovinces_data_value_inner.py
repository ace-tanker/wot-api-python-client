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
from typing import Optional, Set
from typing_extensions import Self

class GlobalmapClanprovincesDataValueInner(BaseModel):
    """
    GlobalmapClanprovincesDataValueInner
    """ # noqa: E501
    arena_id: StrictStr = Field(description="Map ID")
    arena_name: StrictStr = Field(description="Localized map name")
    daily_revenue: StrictInt = Field(description="Daily income")
    front_id: StrictStr = Field(description="Front ID")
    front_name: StrictStr = Field(description="Front name")
    revenue_level: StrictInt = Field(description="Income level from 0 to 11. 0 value means that income was not raised.")
    prime_time: StrictStr = Field(description="Prime Time in UTC")
    province_id: StrictStr = Field(description="Province ID")
    province_name: StrictStr = Field(description="Province name")
    clan_id: StrictInt = Field(description="Clan ID")
    landing_type: Optional[StrictStr] = Field(description="Indicates the landing type of a province")
    turns_owned: StrictInt = Field(description="Province owned (number of turns)")
    max_vehicle_level: StrictInt = Field(description="Maximum vehicle Tier in a Front")
    private: Optional[Any] = Field(description="Restricted province information")
    pillage_end_at: Optional[StrictStr] = Field(description="Date when province will restore its revenue after ransack")
    __properties: ClassVar[List[str]] = ["arena_id", "arena_name", "daily_revenue", "front_id", "front_name", "revenue_level", "prime_time", "province_id", "province_name", "clan_id", "landing_type", "turns_owned", "max_vehicle_level", "private", "pillage_end_at"]

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
        """Create an instance of GlobalmapClanprovincesDataValueInner from a JSON string"""
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
        # set to None if landing_type (nullable) is None
        # and model_fields_set contains the field
        if self.landing_type is None and "landing_type" in self.model_fields_set:
            _dict['landing_type'] = None

        # set to None if private (nullable) is None
        # and model_fields_set contains the field
        if self.private is None and "private" in self.model_fields_set:
            _dict['private'] = None

        # set to None if pillage_end_at (nullable) is None
        # and model_fields_set contains the field
        if self.pillage_end_at is None and "pillage_end_at" in self.model_fields_set:
            _dict['pillage_end_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GlobalmapClanprovincesDataValueInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "arena_id": obj.get("arena_id"),
            "arena_name": obj.get("arena_name"),
            "daily_revenue": obj.get("daily_revenue"),
            "front_id": obj.get("front_id"),
            "front_name": obj.get("front_name"),
            "revenue_level": obj.get("revenue_level"),
            "prime_time": obj.get("prime_time"),
            "province_id": obj.get("province_id"),
            "province_name": obj.get("province_name"),
            "clan_id": obj.get("clan_id"),
            "landing_type": obj.get("landing_type"),
            "turns_owned": obj.get("turns_owned"),
            "max_vehicle_level": obj.get("max_vehicle_level"),
            "private": obj.get("private"),
            "pillage_end_at": obj.get("pillage_end_at")
        })
        return _obj


