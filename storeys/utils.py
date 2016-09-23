# -*- coding: utf-8 -*-
import os
import ast
import shutil
from django.template import loader
from django.template.loader import render_to_string


class StoreysUrlsParseException(Exception):

    def __str__(self):
        return str(self)


class StoreysUrlRefValueException(ValueError):

    def __init__(self, error_message):
        super(ValueError, self).__init__(error_message)


def parse_ast_tree(source, ne_names, ne_module_names):
    try:
        return parse_node(ast.parse(source), [], ne_names, ne_module_names)
    except Exception:
        print 'Parse error'
        raise Exception


def parse_node(node, p_result, ne_names, ne_module_names, pattern_flag=False):
    """
    Recursive parser for nodes in AST.
    Trying to find url-expressions with 'TemplateView.as_view',
    'StoreysView.as_view' or 'include()'
    """
    if pattern_flag and len(node._fields) > 1 and \
            len(node.args) > 1 and (isinstance(node.args[1], ast.Call)):

        if ((hasattr(node.args[1].func, 'id') and node.args[1].func.id == 'include') or
                (hasattr(node.args[1].func, 'value') and
                 (node.args[1].func.value.id == 'TemplateView' or
                  node.args[1].func.value.id == 'StoreysView')
                 and node.args[1].func.attr == 'as_view')) \
                and not node_excluded_by_name(node.keywords, ne_names) \
                and not node_excluded_by_module_name(ast.dump(node), ne_module_names):
            p_result.append(parse_url_node(node))
    elif isinstance(node, ast.Call):
        try:
            if node.func.id == 'patterns':
                for cf in node.args:
                    parse_node(cf, p_result, ne_names,
                               ne_module_names, pattern_flag=True)
        except Exception as e:
            print str(e)
            pass
    elif isinstance(node, list):
        for node_child in node:
            parse_node(node_child, p_result, ne_names, ne_module_names)
    elif hasattr(node, '_fields'):
        if isinstance(node._fields, list):
            for child_field in node._fields:
                parse_node(child_field, p_result, ne_names, ne_module_names)
        elif isinstance(node._fields, tuple):
            for child_field in node._fields:
                parse_node(getattr(node, child_field),
                           p_result, ne_names, ne_module_names)
    return p_result


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
                    yield "include('%s')" % (arg.args[0].s).replace('.','/')
                elif isinstance(arg.args[0], ast.Attribute):
                    yield "include('%s')" % ('.'.join(get_recursive_ast_include(arg.args[0], []))).replace('.','/')
    else:
        for arg in node.args:
            if isinstance(arg, ast.Str):
                # escape any special characters for JS RegExp
                yield ("'%s'" % arg.s).replace("\\","\\\\")
            elif isinstance(arg, ast.Call):
                kwargs = []
                for kw_obj in node.args[1].keywords:
                    if kw_obj.arg == 'template_name':
                        loader.get_template(kw_obj.value.s)
                    kwargs.append("'%s'" % kw_obj.value.s)
                yield render_to_string('../templates/storeys_urls_js/js_template.html', {'url': kwargs[0]})
                # yield "%s.%s(%s)" % (
                #     # n_node.value.id,
                #     'view',
                #     n_node.attr,
                #     ', '.join(kwargs)
                # )
    for kwarg in node.keywords:
        yield "'%s'" % kwarg.value.s


def get_recursive_ast_include(node, arr):
    if hasattr(node, 'attr'):
        arr.append(node.attr)
        return get_recursive_ast_include(node.value, arr)
    else:
        arr.append(node.id)
        arr.reverse()
        return arr


def node_excluded_by_name(node_keywords, excluded_names):
    node_keywords_arr = [ast.dump(kwarg) for kwarg in node_keywords]
    for ex_name in excluded_names:
        for kwarg in node_keywords_arr:
            if "arg='name', value=Str(s='%s')" % ex_name in kwarg:
                return True
    return False


def node_excluded_by_module_name(node, excluded_module_names):
    for ex_module_name in excluded_module_names:
        if "Call(func=Name(id='include', ctx=Load()), args=[Str(s='%s')]" % ex_module_name in node:
            return True

        module_name_arr = ex_module_name.split('.')
        module_name_arr.reverse()
        if "Call(func=Name(id='include', ctx=Load()), args=[%s)]" % get_recursive_attrs(module_name_arr) in node:
            return True
    return False


def get_recursive_attrs(names_arr, string=''):
    if len(names_arr):
        el = names_arr[-1]
        names_arr.remove(el)
        if not string:
            return get_recursive_attrs(
                names_arr,
                string="Name(id='%s', ctx=Load()" % el
            )
        return get_recursive_attrs(
            names_arr,
            string="Attribute(value=%s), attr='%s', ctx=Load()" % (string, el)
        )
    return string


def urlref(name='', module_name=''):
    if not name and not module_name:
        raise StoreysUrlRefValueException(
            "The parameters 'name' and 'module_name' cannot be an empty string")
    if name and module_name:
        raise StoreysUrlRefValueException(
            "Function permits only 'name' OR 'module_name' to be set")
    if not isinstance(name, str) or not isinstance(name, str):
        raise StoreysUrlRefValueException(
            "Input values should be a string")
    if name:
        return {'name': name}
    return {'module_name': module_name}
