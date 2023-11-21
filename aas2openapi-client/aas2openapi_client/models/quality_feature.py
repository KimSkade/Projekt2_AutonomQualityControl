from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.result import Result


T = TypeVar("T", bound="QualityFeature")


@attr.s(auto_attribs=True)
class QualityFeature:
    """
    Attributes:
        id_short (str):
        feature_type (str):
        function (str):
        inspection_equipment (str):
        unit (str):
        upper_warning_limit (float):
        lower_warning_limit (float):
        upper_control_limit (float):
        lower_control_limit (float):
        target_value (float):
        upper_tolerance (float):
        lower_tolerance (float):
        result (Result):
        description (Union[Unset, str]):
        semantic_id (Union[Unset, str]):
        sample_size (Union[Unset, int]):
    """

    id_short: str
    feature_type: str
    function: str
    inspection_equipment: str
    unit: str
    upper_warning_limit: float
    lower_warning_limit: float
    upper_control_limit: float
    lower_control_limit: float
    target_value: float
    upper_tolerance: float
    lower_tolerance: float
    result: "Result"
    description: Union[Unset, str] = UNSET
    semantic_id: Union[Unset, str] = UNSET
    sample_size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_short = self.id_short
        feature_type = self.feature_type
        function = self.function
        inspection_equipment = self.inspection_equipment
        unit = self.unit
        upper_warning_limit = self.upper_warning_limit
        lower_warning_limit = self.lower_warning_limit
        upper_control_limit = self.upper_control_limit
        lower_control_limit = self.lower_control_limit
        target_value = self.target_value
        upper_tolerance = self.upper_tolerance
        lower_tolerance = self.lower_tolerance
        result = self.result.to_dict()

        description = self.description
        semantic_id = self.semantic_id
        sample_size = self.sample_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_short": id_short,
                "feature_type": feature_type,
                "function": function,
                "inspection_equipment": inspection_equipment,
                "unit": unit,
                "upper_warning_limit": upper_warning_limit,
                "lower_warning_limit": lower_warning_limit,
                "upper_control_limit": upper_control_limit,
                "lower_control_limit": lower_control_limit,
                "target_value": target_value,
                "upper_tolerance": upper_tolerance,
                "lower_tolerance": lower_tolerance,
                "result": result,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if semantic_id is not UNSET:
            field_dict["semantic_id"] = semantic_id
        if sample_size is not UNSET:
            field_dict["sample_size"] = sample_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.result import Result

        d = src_dict.copy()
        id_short = d.pop("id_short")

        feature_type = d.pop("feature_type")

        function = d.pop("function")

        inspection_equipment = d.pop("inspection_equipment")

        unit = d.pop("unit")

        upper_warning_limit = d.pop("upper_warning_limit")

        lower_warning_limit = d.pop("lower_warning_limit")

        upper_control_limit = d.pop("upper_control_limit")

        lower_control_limit = d.pop("lower_control_limit")

        target_value = d.pop("target_value")

        upper_tolerance = d.pop("upper_tolerance")

        lower_tolerance = d.pop("lower_tolerance")

        result = Result.from_dict(d.pop("result"))

        description = d.pop("description", UNSET)

        semantic_id = d.pop("semantic_id", UNSET)

        sample_size = d.pop("sample_size", UNSET)

        quality_feature = cls(
            id_short=id_short,
            feature_type=feature_type,
            function=function,
            inspection_equipment=inspection_equipment,
            unit=unit,
            upper_warning_limit=upper_warning_limit,
            lower_warning_limit=lower_warning_limit,
            upper_control_limit=upper_control_limit,
            lower_control_limit=lower_control_limit,
            target_value=target_value,
            upper_tolerance=upper_tolerance,
            lower_tolerance=lower_tolerance,
            result=result,
            description=description,
            semantic_id=semantic_id,
            sample_size=sample_size,
        )

        quality_feature.additional_properties = d
        return quality_feature

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
