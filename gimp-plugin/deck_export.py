#!/usr/bin/env python

from gimpfu import *
import os
import gettext

#  Lokalisierung vorbereiten
gettext.install("deck_of_cards", localedir="locale")
_ = gettext.gettext

#  Plugin-Hauptfunktion
def export_card(image, drawable):
    pdb.gimp_image_undo_group_start(image)

    #  Sichtbare Ebenen kopieren
    temp_image = pdb.gimp_image_duplicate(image)
    visible_layers = [layer for layer in temp_image.layers if pdb.gimp_item_get_visible(layer)]

    # Nur sichtbare Ebenen zusammenführen
    if len(visible_layers) > 1:
        merged = pdb.gimp_image_merge_visible_layers(temp_image, CLIP_TO_IMAGE)
    else:
        merged = visible_layers[0]

    #  Alpha-Kanal aktivieren
    if not pdb.gimp_drawable_has_alpha(merged):
        pdb.gimp_layer_add_alpha(merged)

    #  Dateiname und Pfad festlegen
    export_dir = os.path.expanduser("~/deck_output")  # Zielordner
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)

    # Kartenwert & Symbol aus Ebenennamen extrahieren (Optional – später automatisierbar)
    value_layer = pdb.gimp_image_get_layer_by_name(image, "Card_Value_Top")
    symbol_layer = pdb.gimp_image_get_layer_by_name(image, "Card_Symbol_Top")

    value_text = pdb.gimp_text_layer_get_text(value_layer) if value_layer else "X"
    symbol_text = pdb.gimp_text_layer_get_text(symbol_layer) if symbol_layer else "?"

    filename = f"{value_text}_{symbol_text}.png"
    fullpath = os.path.join(export_dir, filename)

    # ️ Exportieren
    pdb.file_png_save(temp_image, merged, fullpath, filename, 0, 9, 1, 1, 1, 1, 1)

    #  Aufräumen
    pdb.gimp_image_delete(temp_image)
    pdb.gimp_image_undo_group_end(image)

    pdb.gimp_message(_("Card exported to: ") + fullpath)

#  Plugin-Registrierung
register(
    "deck_of_cards_export",
    _("Export visible card layers as PNG"),
    _("Exports visible layers (frame, value, symbol, art) as a transparent PNG"),
    "Kir Nova",
    "MIT License",
    "2025",
    _("Export Card..."),
    "*",  # Unterstützte Bildtypen
    [],   # Keine Parameter notwendig
    [],
    export_card,
    menu=_("<image>/Deck of Cards")
)

main()
