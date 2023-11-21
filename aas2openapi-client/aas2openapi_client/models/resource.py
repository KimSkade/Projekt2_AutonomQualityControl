from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.machine_parameter import MachineParameter
    from ..models.new_machine_parameter import NewMachineParameter


T = TypeVar("T", bound="Resource")


@attr.s(auto_attribs=True)
class Resource:
    """
    Attributes:
        id (str):
        machine_parameter (List['MachineParameter']):
        new_machine_parameter (NewMachineParameter):
        description (Union[Unset, str]):
        id_short (Union[Unset, str]):
        semantic_id (Union[Unset, str]):
    """

    id: str
    machine_parameter: List["MachineParameter"]
    new_machine_parameter: "NewMachineParameter"
    description: Union[Unset, str] = UNSET
    id_short: Union[Unset, str] = UNSET
    semantic_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        machine_parameter = []
        for machine_parameter_item_data in self.machine_parameter:
            machine_parameter_item = machine_parameter_item_data.to_dict()

            machine_parameter.append(machine_parameter_item)

        new_machine_parameter = self.new_machine_parameter.to_dict()

        description = self.description
        id_short = self.id_short
        semantic_id = self.semantic_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_": id,
                "machine_parameter": machine_parameter,
                "new_machine_parameter": new_machine_parameter,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if id_short is not UNSET:
            field_dict["id_short"] = id_short
        if semantic_id is not UNSET:
            field_dict["semantic_id"] = semantic_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.machine_parameter import MachineParameter
        from ..models.new_machine_parameter import NewMachineParameter

        d = src_dict.copy()
        id = d.pop("id_")

        machine_parameter = []
        _machine_parameter = d.pop("machine_parameter")
        for machine_parameter_item_data in _machine_parameter:
            machine_parameter_item = MachineParameter.from_dict(machine_parameter_item_data)

            machine_parameter.append(machine_parameter_item)

        new_machine_parameter = NewMachineParameter.from_dict(d.pop("new_machine_parameter"))

        description = d.pop("description", UNSET)

        id_short = d.pop("id_short", UNSET)

        semantic_id = d.pop("semantic_id", UNSET)

        resource = cls(
            id=id,
            machine_parameter=machine_parameter,
            new_machine_parameter=new_machine_parameter,
            description=description,
            id_short=id_short,
            semantic_id=semantic_id,
        )

        resource.additional_properties = d
        return resource

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
