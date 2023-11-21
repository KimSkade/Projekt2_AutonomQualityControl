from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewResults")


@attr.s(auto_attribs=True)
class NewResults:
    """
    Attributes:
        id_short (str):
        measurement_date (str):
        value (float):
        result_check (bool):
        part_counter (str):
        description (Union[Unset, str]):
        semantic_id (Union[Unset, str]):
        sample_number (Union[Unset, str]):
    """

    id_short: str
    measurement_date: str
    value: float
    result_check: bool
    part_counter: str
    description: Union[Unset, str] = UNSET
    semantic_id: Union[Unset, str] = UNSET
    sample_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_short = self.id_short
        measurement_date = self.measurement_date
        value = self.value
        result_check = self.result_check
        part_counter = self.part_counter
        description = self.description
        semantic_id = self.semantic_id
        sample_number = self.sample_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_short": id_short,
                "measurement_date": measurement_date,
                "value": value,
                "result_check": result_check,
                "part_counter": part_counter,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if semantic_id is not UNSET:
            field_dict["semantic_id"] = semantic_id
        if sample_number is not UNSET:
            field_dict["sample_number"] = sample_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id_short = d.pop("id_short")

        measurement_date = d.pop("measurement_date")

        value = d.pop("value")

        result_check = d.pop("result_check")

        part_counter = d.pop("part_counter")

        description = d.pop("description", UNSET)

        semantic_id = d.pop("semantic_id", UNSET)

        sample_number = d.pop("sample_number", UNSET)

        new_results = cls(
            id_short=id_short,
            measurement_date=measurement_date,
            value=value,
            result_check=result_check,
            part_counter=part_counter,
            description=description,
            semantic_id=semantic_id,
            sample_number=sample_number,
        )

        new_results.additional_properties = d
        return new_results

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
