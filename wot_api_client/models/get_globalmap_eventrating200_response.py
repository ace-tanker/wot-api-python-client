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
from typing import Any, List, Optional
from wot_api_client.models.globalmap_eventrating_error import GlobalmapEventratingError
from wot_api_client.models.globalmap_eventrating_ok import GlobalmapEventratingOk
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

GETGLOBALMAPEVENTRATING200RESPONSE_ONE_OF_SCHEMAS = ["GlobalmapEventratingError", "GlobalmapEventratingOk"]

class GetGlobalmapEventrating200Response(BaseModel):
    """
    GetGlobalmapEventrating200Response
    """
    # data type: GlobalmapEventratingOk
    oneof_schema_1_validator: Optional[GlobalmapEventratingOk] = None
    # data type: GlobalmapEventratingError
    oneof_schema_2_validator: Optional[GlobalmapEventratingError] = None
    actual_instance: Optional[Union[GlobalmapEventratingError, GlobalmapEventratingOk]] = None
    one_of_schemas: Set[str] = { "GlobalmapEventratingError", "GlobalmapEventratingOk" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

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
        instance = GetGlobalmapEventrating200Response.model_construct()
        error_messages = []
        match = 0
        # validate data type: GlobalmapEventratingOk
        if not isinstance(v, GlobalmapEventratingOk):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GlobalmapEventratingOk`")
        else:
            match += 1
        # validate data type: GlobalmapEventratingError
        if not isinstance(v, GlobalmapEventratingError):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GlobalmapEventratingError`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in GetGlobalmapEventrating200Response with oneOf schemas: GlobalmapEventratingError, GlobalmapEventratingOk. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in GetGlobalmapEventrating200Response with oneOf schemas: GlobalmapEventratingError, GlobalmapEventratingOk. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("status")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `status` in the input.")

        # check if data type is `GlobalmapEventratingError`
        if _data_type == "globalmap_eventrating_error":
            instance.actual_instance = GlobalmapEventratingError.from_json(json_str)
            return instance

        # check if data type is `GlobalmapEventratingOk`
        if _data_type == "globalmap_eventrating_ok":
            instance.actual_instance = GlobalmapEventratingOk.from_json(json_str)
            return instance

        # deserialize data into GlobalmapEventratingOk
        try:
            instance.actual_instance = GlobalmapEventratingOk.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GlobalmapEventratingError
        try:
            instance.actual_instance = GlobalmapEventratingError.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into GetGlobalmapEventrating200Response with oneOf schemas: GlobalmapEventratingError, GlobalmapEventratingOk. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GetGlobalmapEventrating200Response with oneOf schemas: GlobalmapEventratingError, GlobalmapEventratingOk. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], GlobalmapEventratingError, GlobalmapEventratingOk]]:
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


