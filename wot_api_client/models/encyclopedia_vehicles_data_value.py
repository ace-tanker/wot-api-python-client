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
from wot_api_client.models.encyclopedia_vehicles_data_value_crew_inner import EncyclopediaVehiclesDataValueCrewInner
from wot_api_client.models.encyclopedia_vehicles_data_value_default_profile import EncyclopediaVehiclesDataValueDefaultProfile
from wot_api_client.models.encyclopedia_vehicles_data_value_images import EncyclopediaVehiclesDataValueImages
from wot_api_client.models.encyclopedia_vehicles_data_value_modules_tree_value import EncyclopediaVehiclesDataValueModulesTreeValue
from wot_api_client.models.encyclopedia_vehicles_data_value_multination_value import EncyclopediaVehiclesDataValueMultinationValue
from typing import Optional, Set
from typing_extensions import Self

class EncyclopediaVehiclesDataValue(BaseModel):
    """
    EncyclopediaVehiclesDataValue
    """ # noqa: E501
    tank_id: StrictInt = Field(description="Vehicle ID")
    type: StrictStr = Field(description="Vehicle type")
    tag: StrictStr = Field(description="Vehicle tag")
    name: StrictStr = Field(description="Vehicle name")
    short_name: StrictStr = Field(description="Vehicle short name")
    description: StrictStr = Field(description="Vehicle description")
    nation: StrictStr = Field(description="Nation")
    tier: StrictInt = Field(description="Tier")
    is_premium: StrictBool = Field(description="Indicates if the vehicle is Premium vehicle")
    is_gift: StrictBool = Field(description="Indicates if the vehicle is a gift vehicle")
    is_wheeled: StrictBool = Field(description="Indicates if the vehicle is a wheeled vehicle")
    is_premium_igr: StrictBool = Field(description="Indicates the IGR vehicle. Active only for Korea realm")
    images: Optional[EncyclopediaVehiclesDataValueImages]
    price_credit: Optional[StrictInt] = Field(description="Cost in credits")
    price_gold: Optional[StrictInt] = Field(description="Cost in gold")
    prices_xp: Optional[Dict[str, StrictInt]] = Field(description="List of research costs in form of pairs:  * parent vehicle ID * cost of research in XP")
    next_tanks: Optional[Dict[str, StrictInt]] = Field(description="List of vehicles available for research in form of pairs:  * researched vehicle ID * cost of research in XP")
    default_profile: Optional[EncyclopediaVehiclesDataValueDefaultProfile]
    guns: List[StrictInt] = Field(description="List of compatible gun IDs")
    turrets: List[StrictInt] = Field(description="List of compatible turret IDs")
    engines: List[StrictInt] = Field(description="List of compatible engine IDs")
    suspensions: List[StrictInt] = Field(description="List of compatible suspension IDs")
    radios: List[StrictInt] = Field(description="List of compatible radio IDs")
    provisions: List[StrictInt] = Field(description="List of IDs of compatible equipment and consumables")
    modules_tree: Optional[Dict[str, Optional[EncyclopediaVehiclesDataValueModulesTreeValue]]] = Field(description="Module research information")
    crew: Optional[List[Optional[EncyclopediaVehiclesDataValueCrewInner]]] = Field(description="Crew")
    multination: Optional[Dict[str, Optional[EncyclopediaVehiclesDataValueMultinationValue]]] = Field(description="Информация об мультинации")
    __properties: ClassVar[List[str]] = ["tank_id", "type", "tag", "name", "short_name", "description", "nation", "tier", "is_premium", "is_gift", "is_wheeled", "is_premium_igr", "images", "price_credit", "price_gold", "prices_xp", "next_tanks", "default_profile", "guns", "turrets", "engines", "suspensions", "radios", "provisions", "modules_tree", "crew", "multination"]

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
        """Create an instance of EncyclopediaVehiclesDataValue from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of images
        if self.images:
            _dict['images'] = self.images.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_profile
        if self.default_profile:
            _dict['default_profile'] = self.default_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in modules_tree (dict)
        _field_dict = {}
        if self.modules_tree:
            for _key_modules_tree in self.modules_tree:
                if self.modules_tree[_key_modules_tree]:
                    _field_dict[_key_modules_tree] = self.modules_tree[_key_modules_tree].to_dict()
            _dict['modules_tree'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in crew (list)
        _items = []
        if self.crew:
            for _item_crew in self.crew:
                if _item_crew:
                    _items.append(_item_crew.to_dict())
            _dict['crew'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in multination (dict)
        _field_dict = {}
        if self.multination:
            for _key_multination in self.multination:
                if self.multination[_key_multination]:
                    _field_dict[_key_multination] = self.multination[_key_multination].to_dict()
            _dict['multination'] = _field_dict
        # set to None if images (nullable) is None
        # and model_fields_set contains the field
        if self.images is None and "images" in self.model_fields_set:
            _dict['images'] = None

        # set to None if price_credit (nullable) is None
        # and model_fields_set contains the field
        if self.price_credit is None and "price_credit" in self.model_fields_set:
            _dict['price_credit'] = None

        # set to None if price_gold (nullable) is None
        # and model_fields_set contains the field
        if self.price_gold is None and "price_gold" in self.model_fields_set:
            _dict['price_gold'] = None

        # set to None if prices_xp (nullable) is None
        # and model_fields_set contains the field
        if self.prices_xp is None and "prices_xp" in self.model_fields_set:
            _dict['prices_xp'] = None

        # set to None if next_tanks (nullable) is None
        # and model_fields_set contains the field
        if self.next_tanks is None and "next_tanks" in self.model_fields_set:
            _dict['next_tanks'] = None

        # set to None if default_profile (nullable) is None
        # and model_fields_set contains the field
        if self.default_profile is None and "default_profile" in self.model_fields_set:
            _dict['default_profile'] = None

        # set to None if modules_tree (nullable) is None
        # and model_fields_set contains the field
        if self.modules_tree is None and "modules_tree" in self.model_fields_set:
            _dict['modules_tree'] = None

        # set to None if crew (nullable) is None
        # and model_fields_set contains the field
        if self.crew is None and "crew" in self.model_fields_set:
            _dict['crew'] = None

        # set to None if multination (nullable) is None
        # and model_fields_set contains the field
        if self.multination is None and "multination" in self.model_fields_set:
            _dict['multination'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EncyclopediaVehiclesDataValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tank_id": obj.get("tank_id"),
            "type": obj.get("type"),
            "tag": obj.get("tag"),
            "name": obj.get("name"),
            "short_name": obj.get("short_name"),
            "description": obj.get("description"),
            "nation": obj.get("nation"),
            "tier": obj.get("tier"),
            "is_premium": obj.get("is_premium"),
            "is_gift": obj.get("is_gift"),
            "is_wheeled": obj.get("is_wheeled"),
            "is_premium_igr": obj.get("is_premium_igr"),
            "images": EncyclopediaVehiclesDataValueImages.from_dict(obj["images"]) if obj.get("images") is not None else None,
            "price_credit": obj.get("price_credit"),
            "price_gold": obj.get("price_gold"),
            "prices_xp": obj.get("prices_xp"),
            "next_tanks": obj.get("next_tanks"),
            "default_profile": EncyclopediaVehiclesDataValueDefaultProfile.from_dict(obj["default_profile"]) if obj.get("default_profile") is not None else None,
            "guns": obj.get("guns"),
            "turrets": obj.get("turrets"),
            "engines": obj.get("engines"),
            "suspensions": obj.get("suspensions"),
            "radios": obj.get("radios"),
            "provisions": obj.get("provisions"),
            "modules_tree": dict(
                (_k, EncyclopediaVehiclesDataValueModulesTreeValue.from_dict(_v))
                for _k, _v in obj["modules_tree"].items()
            )
            if obj.get("modules_tree") is not None
            else None,
            "crew": [EncyclopediaVehiclesDataValueCrewInner.from_dict(_item) for _item in obj["crew"]] if obj.get("crew") is not None else None,
            "multination": dict(
                (_k, EncyclopediaVehiclesDataValueMultinationValue.from_dict(_v))
                for _k, _v in obj["multination"].items()
            )
            if obj.get("multination") is not None
            else None
        })
        return _obj


