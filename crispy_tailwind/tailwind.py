# todo
# 1: this file needs a tidy up
# 2: is this the right implementation. Maybe we can use class converters?

import re

from django.forms import Field, Widget, boundfield


class CSSContainer:
    def __init__(self, css_styles):
        default_items = [
            # widgets
            "text",
            "number",
            "email",
            "url",
            "password",
            "hidden",
            "multiplehidden",
            "file",
            "clearablefile",
            "textarea",
            "date",
            "datetime",
            "time",
            "checkbox",
            "select",
            "nullbooleanselect",
            "selectmultiple",
            "radioselect",
            "checkboxselectmultiple",
            "multi",
            "splitdatetime",
            "splithiddendatetime",
            "selectdate",
            # other items
            "error_border",
        ]

        base = css_styles.get("base", "")
        for item in default_items:
            setattr(self, item, base)

        for key, value in css_styles.items():
            if key != "base":
                # get current attribute and rejoin with a set, also to ensure a space between each attribute
                current_class = set(getattr(self, key).split())
                current_class.update(set(value.split()))
                new_classes = " ".join(current_class)
                setattr(self, key, new_classes)

    def __repr__(self):
        return str(self.__dict__)

    def __add__(self, other):
        for field, css_class in other.items():
            current_class = set(getattr(self, field).split())
            current_class.update(set(css_class.split()))
            new_classes = " ".join(current_class)
            setattr(self, field, new_classes)
        return self

    def __sub__(self, other):
        for field, css_class in other.items():
            current_class = set(getattr(self, field).split())
            removed_classes = set(css_class.split())
            new_classes = " ".join(current_class - removed_classes)
            setattr(self, field, new_classes)
        return self

    def get_input_class(self, obj):
        # Following check is used to keep backward compatibility with older versions
        if isinstance(obj, boundfield.BoundField):
            widget = obj.field.widget
        elif isinstance(obj, Field):
            widget = obj.widget
        elif isinstance(obj, Widget):
            widget = obj
        else:
            raise ValueError("Object must be a BoundField, Field or Widget")
        widget_name = re.sub(r"widget$|input$", "", widget.__class__.__name__.lower())
        return getattr(self, widget_name, "")
