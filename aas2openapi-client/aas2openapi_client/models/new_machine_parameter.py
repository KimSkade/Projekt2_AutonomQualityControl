from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_values_machine_parameter import NewValuesMachineParameter


T = TypeVar("T", bound="NewMachineParameter")


@attr.s(auto_attribs=True)
class NewMachineParameter:
    """
    Attributes:
        id_short (str):
        new_values_machine_parameter (List['NewValuesMachineParameter']):
        description (Union[Unset, str]):
        semantic_id (Union[Unset, str]):
    """

    id_short: str
    new_values_machine_parameter: List["NewValuesMachineParameter"]
    description: Union[Unset, str] = UNSET
    semantic_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_short = self.id_short
        new_values_machine_parameter = []
        for new_values_machine_parameter_item_data in self.new_values_machine_parameter:
            new_values_machine_parameter_item = new_values_machine_parameter_item_data.to_dict()

            new_values_machine_parameter.append(new_values_machine_parameter_item)

        description = self.description
        semantic_id = self.semantic_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_short": id_short,
                "new_values_machine_parameter": new_values_machine_parameter,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if semantic_id is not UNSET:
            field_dict["semantic_id"] = semantic_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.new_values_machine_parameter import NewValuesMachineParameter

        d = src_dict.copy()
        id_short = d.pop("id_short")

        new_values_machine_parameter = []
        _new_values_machine_parameter = d.pop("new_values_machine_parameter")
        for new_values_machine_parameter_item_data in _new_values_machine_parameter:
            new_values_machine_parameter_item = NewValuesMachineParameter.from_dict(
                new_values_machine_parameter_item_data
            )

            new_values_machine_parameter.append(new_values_machine_parameter_item)

        description = d.pop("description", UNSET)

        semantic_id = d.pop("semantic_id", UNSET)

        new_machine_parameter = cls(
            id_short=id_short,
            new_values_machine_parameter=new_values_machine_parameter,
            description=description,
            semantic_id=semantic_id,
        )

        new_machine_parameter.additional_properties = d
        return new_machine_parameter

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
