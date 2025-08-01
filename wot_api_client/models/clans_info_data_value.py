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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wot_api_client.models.clans_info_data_value_members import ClansInfoDataValueMembers
from wot_api_client.models.clans_info_data_value_private import ClansInfoDataValuePrivate
from wot_api_client.models.clans_list_data_inner_emblems import ClansListDataInnerEmblems
from typing import Optional, Set
from typing_extensions import Self

class ClansInfoDataValue(BaseModel):
    """
    ClansInfoDataValue
    """ # noqa: E501
    clan_id: StrictInt = Field(description="Clan ID")
    name: StrictStr = Field(description="Clan name")
    tag: StrictStr = Field(description="Clan tag")
    created_at: StrictInt = Field(description="Clan creation date")
    color: StrictStr = Field(description="Clan color in HEX #RRGGBB")
    members_count: StrictInt = Field(description="Number of clan members")
    emblems: Optional[ClansListDataInnerEmblems]
    old_name: StrictStr = Field(description="Old clan name")
    old_tag: StrictStr = Field(description="Old clan tag")
    renamed_at: StrictInt = Field(description="Time (UTC) when clan name was changed")
    description: StrictStr = Field(description="Clan description")
    description_html: StrictStr = Field(description="Clan description in HTML")
    motto: StrictStr = Field(description="Clan motto")
    is_clan_disbanded: StrictBool = Field(description="Clan has been deleted. The deleted clan data contains valid values for the following fields only: **clan_id**, **is_clan_disbanded**, **updated_at**.")
    accepts_join_requests: StrictBool = Field(description="Clan can invite players")
    updated_at: StrictInt = Field(description="Time when clan details were updated")
    creator_id: StrictInt = Field(description="Clan creator ID")
    creator_name: StrictStr = Field(description="Clan creator's name")
    leader_id: StrictInt = Field(description="Clan Commander ID")
    leader_name: StrictStr = Field(description="Commander's name")
    members: Optional[ClansInfoDataValueMembers]
    private: Optional[ClansInfoDataValuePrivate]
    __properties: ClassVar[List[str]] = ["clan_id", "name", "tag", "created_at", "color", "members_count", "emblems", "old_name", "old_tag", "renamed_at", "description", "description_html", "motto", "is_clan_disbanded", "accepts_join_requests", "updated_at", "creator_id", "creator_name", "leader_id", "leader_name", "members", "private"]

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
        """Create an instance of ClansInfoDataValue from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of emblems
        if self.emblems:
            _dict['emblems'] = self.emblems.to_dict()
        # override the default output from pydantic by calling `to_dict()` of members
        if self.members:
            _dict['members'] = self.members.to_dict()
        # override the default output from pydantic by calling `to_dict()` of private
        if self.private:
            _dict['private'] = self.private.to_dict()
        # set to None if emblems (nullable) is None
        # and model_fields_set contains the field
        if self.emblems is None and "emblems" in self.model_fields_set:
            _dict['emblems'] = None

        # set to None if members (nullable) is None
        # and model_fields_set contains the field
        if self.members is None and "members" in self.model_fields_set:
            _dict['members'] = None

        # set to None if private (nullable) is None
        # and model_fields_set contains the field
        if self.private is None and "private" in self.model_fields_set:
            _dict['private'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClansInfoDataValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clan_id": obj.get("clan_id"),
            "name": obj.get("name"),
            "tag": obj.get("tag"),
            "created_at": obj.get("created_at"),
            "color": obj.get("color"),
            "members_count": obj.get("members_count"),
            "emblems": ClansListDataInnerEmblems.from_dict(obj["emblems"]) if obj.get("emblems") is not None else None,
            "old_name": obj.get("old_name"),
            "old_tag": obj.get("old_tag"),
            "renamed_at": obj.get("renamed_at"),
            "description": obj.get("description"),
            "description_html": obj.get("description_html"),
            "motto": obj.get("motto"),
            "is_clan_disbanded": obj.get("is_clan_disbanded"),
            "accepts_join_requests": obj.get("accepts_join_requests"),
            "updated_at": obj.get("updated_at"),
            "creator_id": obj.get("creator_id"),
            "creator_name": obj.get("creator_name"),
            "leader_id": obj.get("leader_id"),
            "leader_name": obj.get("leader_name"),
            "members": ClansInfoDataValueMembers.from_dict(obj["members"]) if obj.get("members") is not None else None,
            "private": ClansInfoDataValuePrivate.from_dict(obj["private"]) if obj.get("private") is not None else None
        })
        return _obj


