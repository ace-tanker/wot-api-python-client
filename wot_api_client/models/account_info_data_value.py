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
from wot_api_client.models.account_info_data_value_private import AccountInfoDataValuePrivate
from wot_api_client.models.account_info_data_value_statistics import AccountInfoDataValueStatistics
from typing import Optional, Set
from typing_extensions import Self

class AccountInfoDataValue(BaseModel):
    """
    AccountInfoDataValue
    """ # noqa: E501
    statistics: Optional[AccountInfoDataValueStatistics]
    account_id: StrictInt = Field(description="Player account ID")
    created_at: StrictInt = Field(description="Date when player's account was created")
    updated_at: StrictInt = Field(description="Date when player details were updated")
    logout_at: StrictInt = Field(description="End time of last game session")
    last_battle_time: StrictInt = Field(description="Last battle time")
    nickname: StrictStr = Field(description="Player name")
    global_rating: StrictInt = Field(description="Personal rating")
    private: Optional[AccountInfoDataValuePrivate]
    client_language: StrictStr = Field(description="Language selected in the game client")
    clan_id: Optional[StrictInt] = Field(description="Clan ID")
    __properties: ClassVar[List[str]] = ["statistics", "account_id", "created_at", "updated_at", "logout_at", "last_battle_time", "nickname", "global_rating", "private", "client_language", "clan_id"]

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
        """Create an instance of AccountInfoDataValue from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of statistics
        if self.statistics:
            _dict['statistics'] = self.statistics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of private
        if self.private:
            _dict['private'] = self.private.to_dict()
        # set to None if statistics (nullable) is None
        # and model_fields_set contains the field
        if self.statistics is None and "statistics" in self.model_fields_set:
            _dict['statistics'] = None

        # set to None if private (nullable) is None
        # and model_fields_set contains the field
        if self.private is None and "private" in self.model_fields_set:
            _dict['private'] = None

        # set to None if clan_id (nullable) is None
        # and model_fields_set contains the field
        if self.clan_id is None and "clan_id" in self.model_fields_set:
            _dict['clan_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccountInfoDataValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "statistics": AccountInfoDataValueStatistics.from_dict(obj["statistics"]) if obj.get("statistics") is not None else None,
            "account_id": obj.get("account_id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "logout_at": obj.get("logout_at"),
            "last_battle_time": obj.get("last_battle_time"),
            "nickname": obj.get("nickname"),
            "global_rating": obj.get("global_rating"),
            "private": AccountInfoDataValuePrivate.from_dict(obj["private"]) if obj.get("private") is not None else None,
            "client_language": obj.get("client_language"),
            "clan_id": obj.get("clan_id")
        })
        return _obj


