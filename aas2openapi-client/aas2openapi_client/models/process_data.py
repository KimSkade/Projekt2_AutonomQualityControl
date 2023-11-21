from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_values_process_data import NewValuesProcessData


T = TypeVar("T", bound="ProcessData")


@attr.s(auto_attribs=True)
class ProcessData:
    """
    Attributes:
        id_short (str):
        process_data_resource (str):
        features_list (List[str]):
        new_values (List['NewValuesProcessData']):
        description (Union[Unset, str]):
        semantic_id (Union[Unset, str]):
    """

    id_short: str
    process_data_resource: str
    features_list: List[str]
    new_values: List["NewValuesProcessData"]
    description: Union[Unset, str] = UNSET
    semantic_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_short = self.id_short
        process_data_resource = self.process_data_resource
        features_list = self.features_list

        new_values = []
        for new_values_item_data in self.new_values:
            new_values_item = new_values_item_data.to_dict()

            new_values.append(new_values_item)

        description = self.description
        semantic_id = self.semantic_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_short": id_short,
                "process_data_resource": process_data_resource,
                "features_list": features_list,
                "new_values": new_values,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if semantic_id is not UNSET:
            field_dict["semantic_id"] = semantic_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.new_values_process_data import NewValuesProcessData

        d = src_dict.copy()
        id_short = d.pop("id_short")

        process_data_resource = d.pop("process_data_resource")

        features_list = cast(List[str], d.pop("features_list"))

        new_values = []
        _new_values = d.pop("new_values")
        for new_values_item_data in _new_values:
            new_values_item = NewValuesProcessData.from_dict(new_values_item_data)

            new_values.append(new_values_item)

        description = d.pop("description", UNSET)

        semantic_id = d.pop("semantic_id", UNSET)

        process_data = cls(
            id_short=id_short,
            process_data_resource=process_data_resource,
            features_list=features_list,
            new_values=new_values,
            description=description,
            semantic_id=semantic_id,
        )

        process_data.additional_properties = d
        return process_data

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
