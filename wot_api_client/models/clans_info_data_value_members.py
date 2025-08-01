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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, Dict, List, Optional
from wot_api_client.models.clans_info_data_value_members_one_of_inner import ClansInfoDataValueMembersOneOfInner
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

CLANSINFODATAVALUEMEMBERS_ONE_OF_SCHEMAS = ["Dict[str, ClansInfoDataValueMembersOneOfInner]", "List[ClansInfoDataValueMembersOneOfInner]"]

class ClansInfoDataValueMembers(BaseModel):
    """
    Information on clan members. Field format depends on members_key input parameter.
    """
    # data type: List[ClansInfoDataValueMembersOneOfInner]
    oneof_schema_1_validator: Optional[List[Optional[ClansInfoDataValueMembersOneOfInner]]] = None
    # data type: Dict[str, ClansInfoDataValueMembersOneOfInner]
    oneof_schema_2_validator: Optional[Dict[str, Optional[ClansInfoDataValueMembersOneOfInner]]] = None
    actual_instance: Optional[Union[Dict[str, ClansInfoDataValueMembersOneOfInner], List[ClansInfoDataValueMembersOneOfInner]]] = None
    one_of_schemas: Set[str] = { "Dict[str, ClansInfoDataValueMembersOneOfInner]", "List[ClansInfoDataValueMembersOneOfInner]" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        if v is None:
            return v

        instance = ClansInfoDataValueMembers.model_construct()
        error_messages = []
        match = 0
        # validate data type: List[ClansInfoDataValueMembersOneOfInner]
        try:
            instance.oneof_schema_1_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: Dict[str, ClansInfoDataValueMembersOneOfInner]
        try:
            instance.oneof_schema_2_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ClansInfoDataValueMembers with oneOf schemas: Dict[str, ClansInfoDataValueMembersOneOfInner], List[ClansInfoDataValueMembersOneOfInner]. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ClansInfoDataValueMembers with oneOf schemas: Dict[str, ClansInfoDataValueMembersOneOfInner], List[ClansInfoDataValueMembersOneOfInner]. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: Optional[str]) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        if json_str is None:
            return instance

        error_messages = []
        match = 0

        # deserialize data into List[ClansInfoDataValueMembersOneOfInner]
        try:
            # validation
            instance.oneof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_1_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Dict[str, ClansInfoDataValueMembersOneOfInner]
        try:
            # validation
            instance.oneof_schema_2_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_2_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ClansInfoDataValueMembers with oneOf schemas: Dict[str, ClansInfoDataValueMembersOneOfInner], List[ClansInfoDataValueMembersOneOfInner]. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ClansInfoDataValueMembers with oneOf schemas: Dict[str, ClansInfoDataValueMembersOneOfInner], List[ClansInfoDataValueMembersOneOfInner]. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], Dict[str, ClansInfoDataValueMembersOneOfInner], List[ClansInfoDataValueMembersOneOfInner]]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


