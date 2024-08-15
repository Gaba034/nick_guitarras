from core.enums import Builder, TypeG, Wood
from core.instrument_spec import InstrumentSpec


class GuitarSpec(InstrumentSpec):
    def __init__(
        self,
        builder: Builder,
        model: str,
        typeg: TypeG,
        back_wood: Wood,
        top_wood: Wood,
        num_strings,
    ):
        super().__init__(builder, model, typeg, back_wood, top_wood)
        self.num_strings = num_strings

    def get_num_strings(self) -> str:
        return self.num_strings

    def matches(self, other_spec) -> bool:
        if not isinstance(other_spec, GuitarSpec):
            return False

        if self.builder != other_spec.get_builder():
            return False
        if self.model and self.model.lower() != other_spec.get_model().lower():
            return False
        if self.typeg != other_spec.get_typeg():
            return False
        if self.back_wood != other_spec.get_back_wood():
            return False
        if self.top_wood != other_spec.get_top_wood():
            return False
        if self.num_strings != other_spec.get_num_strings():
            return False

        return True
