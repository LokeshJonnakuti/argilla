from typing import Any, Dict

from typing import List


import attr

from ..types import UNSET, Unset

from typing import Dict
from ..models.text_classification_aggregations_inputs_additional_property import (
    TextClassificationAggregationsInputsAdditionalProperty,
)
from typing import cast


@attr.s(auto_attribs=True)
class TextClassificationAggregationsInputs:
    """  """

    additional_properties: Dict[str, TextClassificationAggregationsInputsAdditionalProperty] = attr.ib(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @staticmethod
    def from_dict(src_dict: Dict[str, Any]) -> "TextClassificationAggregationsInputs":
        d = src_dict.copy()
        text_classification_aggregations_inputs = TextClassificationAggregationsInputs()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = TextClassificationAggregationsInputsAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        text_classification_aggregations_inputs.additional_properties = additional_properties
        return text_classification_aggregations_inputs

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> TextClassificationAggregationsInputsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: TextClassificationAggregationsInputsAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties