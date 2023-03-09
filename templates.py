"""
JOHNPRIME TEMPLATES
"""
from functools import cached_property
from typing import Optional

from photoshop.api._artlayer import ArtLayer

from src import templates as temp
from src.constants import con
from src.settings import cfg
import src.helpers as psd


class WomensdayShortTemplate (temp.WomensDayTemplate):
    """
     * Womensday Short Template
     * Created by JohnPrime
    """
    template_file_name = "WomensdayShort"
    template_suffix = "Showcase Short"

    def __init__(self, layout):
        cfg.remove_reminder = True
        cfg.remove_flavor = True
        super().__init__(layout)

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def is_nyx(self) -> bool:
        return False


"""
MDFC TEMPLATES
"""


class BorderlessMDFCBackTemplate (temp.MDFCBackTemplate):
    """
    Borderless version of the MDFC Back template
    """
    template_file_name = "BorderlessMDFCBack"
    dfc_layer_group = con.layers.MDFC_BACK
    template_suffix = "Showcase"

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def is_nyx(self) -> bool:
        return False

    @cached_property
    def art_reference_layer(self) -> ArtLayer:
        # Only Full Art reference
        return psd.getLayer(con.layers.FULL_ART_FRAME)

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        # No backgrounds
        return

    def enable_crown(self) -> None:
        # No borders, no nyx, no companion
        psd.enable_mask(self.pinlines_layer.parent)
        self.crown_layer.visible = True

    def load_artwork(self):
        super().load_artwork()

        # Content aware fill
        psd.content_fill_empty_area(self.art_layer)


class BorderlessMDFCFrontTemplate (BorderlessMDFCBackTemplate):
    """
    Borderless version of the MDFC Front template
    """
    template_file_name = "BorderlessMDFCFront"
    dfc_layer_group = con.layers.MDFC_FRONT
    template_suffix = "Showcase"


"""
Double faced card templates
"""


class BorderlessTFBackTemplate (temp.TransformBackTemplate):
    """
    Template for the back faces of transform cards.
    """
    template_file_name = "BorderlessTFBack"
    dfc_layer_group = con.layers.TF_BACK
    template_suffix = "Borderless"

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def is_nyx(self) -> bool:
        return False

    @cached_property
    def text_layer_name(self) -> Optional[ArtLayer]:
        # CARD NAME
        return psd.getLayer(con.layers.NAME, self.text_layers)

    @cached_property
    def art_reference_layer(self) -> ArtLayer:
        # Only Full Art reference
        return psd.getLayer(con.layers.FULL_ART_FRAME)

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        # No backgrounds
        return

    @cached_property
    def pinlines_layer(self) -> Optional[ArtLayer]:
        # No land pinlines group
        return psd.getLayer(self.layout.pinlines, con.layers.PINLINES_TEXTBOX)

    def enable_crown(self) -> None:
        # No borders, no nyx, no companion
        psd.enable_mask(self.pinlines_layer.parent)
        self.crown_layer.visible = True

    def load_artwork(self):
        super().load_artwork()

        # Content aware fill
        psd.content_fill_empty_area(self.art_layer)


class BorderlessTFFrontTemplate (temp.TransformFrontTemplate):
    """
    Template for the front faces of transform cards.
    """
    template_file_name = "BorderlessTFFront"
    dfc_layer_group = con.layers.TF_FRONT
    template_suffix = "Borderless"

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def is_nyx(self) -> bool:
        return False

    @cached_property
    def text_layer_name(self) -> Optional[ArtLayer]:
        # CARD NAME
        return psd.getLayer(con.layers.NAME, self.text_layers)

    @cached_property
    def art_reference_layer(self) -> ArtLayer:
        # Only Full Art reference
        return psd.getLayer(con.layers.FULL_ART_FRAME)

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        # No backgrounds
        return

    @cached_property
    def pt_layer(self) -> Optional[ArtLayer]:
        # Group must be turned on if needed
        if self.is_creature:
            group = psd.getLayerSet(con.layers.PT_BOX)
            group.visible = True
            return psd.getLayer(self.layout.twins, group)
        return

    def enable_crown(self) -> None:
        # Crown group must be turned on first
        self.crown_layer.parent.visible = True
        psd.enable_mask(self.pinlines_layer.parent)
        self.crown_layer.visible = True

    def load_artwork(self):
        super().load_artwork()

        # Content aware fill
        psd.content_fill_empty_area(self.art_layer)
