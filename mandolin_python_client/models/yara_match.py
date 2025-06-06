# coding: utf-8

"""
    Mandolin

    Micro-service to analyze and convert files

    The version of the OpenAPI document: 1.0.2
    Contact: contact@defensive-lab.agency
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mandolin_python_client.models.yara_string import YaraString
from typing import Optional, Set
from typing_extensions import Self

class YaraMatch(BaseModel):
    """
    YaraMatch
    """ # noqa: E501
    rule: StrictStr
    tags: Optional[List[StrictStr]] = None
    namespace: Optional[StrictStr] = None
    meta: Optional[Dict[str, Any]] = None
    strings: Optional[List[YaraString]] = None
    __properties: ClassVar[List[str]] = ["rule", "tags", "namespace", "meta", "strings"]

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
        """Create an instance of YaraMatch from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in strings (list)
        _items = []
        if self.strings:
            for _item_strings in self.strings:
                if _item_strings:
                    _items.append(_item_strings.to_dict())
            _dict['strings'] = _items
        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if namespace (nullable) is None
        # and model_fields_set contains the field
        if self.namespace is None and "namespace" in self.model_fields_set:
            _dict['namespace'] = None

        # set to None if meta (nullable) is None
        # and model_fields_set contains the field
        if self.meta is None and "meta" in self.model_fields_set:
            _dict['meta'] = None

        # set to None if strings (nullable) is None
        # and model_fields_set contains the field
        if self.strings is None and "strings" in self.model_fields_set:
            _dict['strings'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of YaraMatch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "rule": obj.get("rule"),
            "tags": obj.get("tags"),
            "namespace": obj.get("namespace"),
            "meta": obj.get("meta"),
            "strings": [YaraString.from_dict(_item) for _item in obj["strings"]] if obj.get("strings") is not None else None
        })
        return _obj


