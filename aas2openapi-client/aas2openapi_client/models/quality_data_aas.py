from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.procedure import Procedure
    from ..models.quality_data import QualityData
    from ..models.resource import Resource


T = TypeVar("T", bound="QualityDataAAS")


@attr.s(auto_attribs=True)
class QualityDataAAS:
    """Base class for all Asset Administration Shells (AAS).

    Args:
        id (str): Global id of the object.
        id_short (str): Local id of the object.
        description (str, optional): Description of the object. Defaults to None.

        Attributes:
            id_short (str):
            id (str):
            quality_data (QualityData): Base class for all submodels.

                Args:
                    id (str): Global id of the object.
                    id_short (str): Local id of the object.
                    description (str, optional): Description of the object. Defaults to None.
                    semantic_id (str, optional): Semantic id of the object. Defaults to None.
            procedure (Procedure): Base class for all submodels.

                Args:
                    id (str): Global id of the object.
                    id_short (str): Local id of the object.
                    description (str, optional): Description of the object. Defaults to None.
                    semantic_id (str, optional): Semantic id of the object. Defaults to None.
            resource (Resource): Base class for all submodels.

                Args:
                    id (str): Global id of the object.
                    id_short (str): Local id of the object.
                    description (str, optional): Description of the object. Defaults to None.
                    semantic_id (str, optional): Semantic id of the object. Defaults to None.
            description (Union[Unset, str]):
    """

    id_short: str
    id: str
    quality_data: "QualityData"
    procedure: "Procedure"
    resource: "Resource"
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_short = self.id_short
        id = self.id
        quality_data = self.quality_data.to_dict()

        procedure = self.procedure.to_dict()

        resource = self.resource.to_dict()

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_short": id_short,
                "id": id,
                "quality_data": quality_data,
                "procedure": procedure,
                "resource": resource,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.procedure import Procedure
        from ..models.quality_data import QualityData
        from ..models.resource import Resource

        d = src_dict.copy()
        id_short = d.pop("id_short")

        id = d.pop("id")

        quality_data = QualityData.from_dict(d.pop("quality_data"))

        procedure = Procedure.from_dict(d.pop("procedure"))

        resource = Resource.from_dict(d.pop("resource"))

        description = d.pop("description", UNSET)

        quality_data_aas = cls(
            id_short=id_short,
            id=id,
            quality_data=quality_data,
            procedure=procedure,
            resource=resource,
            description=description,
        )

        quality_data_aas.additional_properties = d
        return quality_data_aas

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
