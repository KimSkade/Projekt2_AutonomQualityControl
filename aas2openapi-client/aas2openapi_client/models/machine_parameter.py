from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MachineParameter")


@attr.s(auto_attribs=True)
class MachineParameter:
    """
    Attributes:
        id_short (str):
        value_min (float):
        value_max (float):
        value_description (str):
        description (Union[Unset, str]):
        semantic_id (Union[Unset, str]):
    """

    id_short: str
    value_min: float
    value_max: float
    value_description: str
    description: Union[Unset, str] = UNSET
    semantic_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_short = self.id_short
        value_min = self.value_min
        value_max = self.value_max
        value_description = self.value_description
        description = self.description
        semantic_id = self.semantic_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_short": id_short,
                "value_min": value_min,
                "value_max": value_max,
                "value_description": value_description,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if semantic_id is not UNSET:
            field_dict["semantic_id"] = semantic_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id_short = d.pop("id_short")

        value_min = d.pop("value_min")

        value_max = d.pop("value_max")

        value_description = d.pop("value_description")

        description = d.pop("description", UNSET)

        semantic_id = d.pop("semantic_id", UNSET)

        machine_parameter = cls(
            id_short=id_short,
            value_min=value_min,
            value_max=value_max,
            value_description=value_description,
            description=description,
            semantic_id=semantic_id,
        )

        machine_parameter.additional_properties = d
        return machine_parameter

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
