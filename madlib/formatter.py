from markdown.core import Markdown

# from pymdownx.superfences import fence_code_format


def _escape(txt):
    """Basic html escaping."""

    txt = txt.replace('&', '&amp;')
    txt = txt.replace('<', '&lt;')
    txt = txt.replace('>', '&gt;')
    return txt


def fence_code_format(source, language, class_name, options, md, **kwargs):
    """Format source as code blocks."""

    classes = kwargs['classes']
    id_value = kwargs['id_value']
    attrs = kwargs['attrs']

    if class_name:
        classes.insert(0, class_name)

    id_value = ' id="{}"'.format(id_value) if id_value else ''
    classes = ' class="{}"'.format(' '.join(classes)) if classes else ''
    attrs = ' ' + ' '.join('{k}="{v}"'.format(k=k, v=v) for k, v in attrs.items()) if attrs else ''

    return '<pre%s%s%s><code>%s</code></pre>' % (id_value, classes, attrs, _escape(source))


def formatter(
    source: str,
    language: str,
    css_class: str,
    options: dict,
    md: Markdown,
    **kwargs,
) -> str:
    """Custom formatter for madlib.

    Args:
        source (str): The content from within the fenced code.
        language (str): The language of the fenced code; madlib.
        css_class (str): The CSS class name; madlib.
        options (dict):
        md (Markdown):

    Returns (str): the formatted HTML string to render.
    """
    print(source)
    print(language)
    print(css_class)
    print(options)

    print(fence_code_format(
        source,
        "terraform",
        css_class,
        options,
        md,
    ))

    return "hello"
