# -*- coding: utf-8 -*-
import ast
from django.template import loader

class StoreysUrlsParseException(Exception):
    def __str__(self):
        return str(self)


def get_recursive_include(node, arr):
    if hasattr(node, 'attr'):
        arr.append(node.attr)
        return get_recursive_include(node.value, arr)
    else:
        arr.append(node.id)
        arr.reverse()
        return arr


def parse_url_node(node):
    """
    Parser for url(...) node of AST.
    """
    n_node = node.args[1].func
    if hasattr(n_node, 'id') and n_node.id == 'include':
        for arg in node.args:
            if isinstance(arg, ast.Str):
                yield "'%s'" % arg.s
            elif isinstance(arg, ast.Call):
                if isinstance(arg.args[0], ast.Str):
                    yield "include('%s')" % arg.args[0].s
                elif isinstance(arg.args[0], ast.Attribute):
                    yield "include('%s')" % '.'.join(get_recursive_include(arg.args[0], []))
    else:
        for arg in node.args:
            if isinstance(arg, ast.Str):
                yield "'%s'" % arg.s
            elif isinstance(arg, ast.Call):
                kwargs = []
                for kw_obj in node.args[1].keywords:
                    if kw_obj.arg == 'template_name':
                        loader.get_template(kw_obj.value.s)
                    kwargs.append("%s='%s'" % (kw_obj.arg, kw_obj.value.s))
                yield "%s.%s(%s)" % (
                    n_node.value.id,
                    n_node.attr,
                    ', '.join(kwargs)
                )
    for kwarg in node.keywords:
        yield "%s='%s'" % (kwarg.arg, kwarg.value.s)


def parse_node(node, p_result, pattern_flag=False):
    """
    Recursive parser for nodes in AST.
    Trying to find url-expressions with 'TemplateView.as_view',
    'StoreysView.as_view' or 'include()'
    """
    if pattern_flag and len(node._fields) > 1 and \
            len(node.args) > 1 and (isinstance(node.args[1], ast.Call)):
        if (hasattr(node.args[1].func, 'id') and node.args[1].func.id == 'include') or\
           (hasattr(node.args[1].func, 'value') and
                (node.args[1].func.value.id == 'TemplateView' or
                 node.args[1].func.value.id == 'StoreysView') and
                node.args[1].func.attr == 'as_view'):
            p_result.append(parse_url_node(node))
    elif isinstance(node, ast.Call):
        try:
            if node.func.id == 'patterns':
                for cf in node.args:
                    parse_node(cf, p_result, pattern_flag=True)
        except Exception as e:
            print str(e)
            pass
    elif isinstance(node, list):
        for node_child in node:
            parse_node(node_child, p_result)
    elif hasattr(node, '_fields'):
        if isinstance(node._fields, list):
            for child_field in node._fields:
                parse_node(child_field, p_result, sname)
        elif isinstance(node._fields, tuple):
            for child_field in node._fields:
                parse_node(getattr(node, child_field), p_result)
    return p_result


def parse_ast_tree(source):
    try:
        return parse_node(ast.parse(source), [])
    except Exception:
        print 'Parse error'
