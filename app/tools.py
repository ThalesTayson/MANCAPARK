
def formToJson(form):
    data = {}
    fields = form.fields.keys()
    for field in fields:
        obj_field = form.fields.get(field)
        data.setdefault(field, {})
        data[field].setdefault('input_type', obj_field.widget.input_type)
        data[field].setdefault('is_hidden', obj_field.widget.is_hidden)
        data[field].setdefault('is_required', obj_field.widget.is_required)
        data[field].setdefault('attrs', obj_field.widget.attrs)
    return data