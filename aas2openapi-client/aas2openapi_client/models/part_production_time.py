from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartProductionTime")


@attr.s(auto_attribs=True)
class PartProductionTime:
    """
    Attributes:
        id_short (str):
        timestamp (str):
        part_counter (int):
        description (Union[Unset, str]):
        semantic_id (Union[Unset, str]):
    """

    id_short: str
    timestamp: str
    part_counter: int
    description: Union[Unset, str] = UNSET
    semantic_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_short = self.id_short
        timestamp = self.timestamp
        part_counter = self.part_counter
        description = self.description
        semantic_id = self.semantic_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_short": id_short,
                "timestamp": timestamp,
                "part_counter": part_counter,
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

        timestamp = d.pop("timestamp")

        part_counter = d.pop("part_counter")

        description = d.pop("description", UNSET)

        semantic_id = d.pop("semantic_id", UNSET)

        part_production_time = cls(
            id_short=id_short,
            timestamp=timestamp,
            part_counter=part_counter,
            description=description,
            semantic_id=semantic_id,
        )

        part_production_time.additional_properties = d
        return part_production_time

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
