""" This module contains different import utility tools """

import importlib


class ImportUtils:
    """ Import utils class """

    @staticmethod
    def raise_exception_if_module_not_exists(module_name: str, msg: str = None):
        """
            Method that raise an exception if the module does not exist.

        :param module_name: Name of module.
        :param msg: [Optional] Raise exception.
        """
        MODULE_NOT_EXISTS = f"Module '{module_name}' does not exist. Please add it!"
        if not ImportUtils.module_exists(module_name):
            raise ModuleNotFoundError(msg if msg is not None else MODULE_NOT_EXISTS)

    @staticmethod
    def module_exists(module_name: str, package_name: str = None) -> bool:
        """
            Method that returns the existence or not of a module.

        The 'package_name' argument is required when performing a relative import. It
        specifies the package to use as the anchor point from which to resolve the
        relative import to an absolute import.

            True -> Correct module.
            False -> Incorrect module.

        :param package_name: Package name
        :param module_name: Module name.
        :return: [Bool] Response.
        """

        try:
            importlib.import_module(name=module_name, package=package_name)
            return True
        except ModuleNotFoundError:
            return False

    @staticmethod
    def fullname(_object: object) -> str:
        """
            Method that returns the fully qualified class name for a object.

        :param _object: Input object.
        :return: [Str] Fully qualified class name
        """
        module_name = _object.__class__.__module__
        class_name = _object.__class__.__name__
        if module_name is None or module_name == str.__class__.__module__:
            return class_name  # Avoid reporting __builtin__
        else:
            return '.'.join([module_name, class_name])

    @staticmethod
    def get_parts_of_fullname(fullname: str) -> dict:
        """
            Method that returns the parts of fullname.

        :param fullname: fully qualified class name for a object
        :return: [Dict] Parts of fullname
        """
        parts_of_fullname = fullname.split('.')
        if len(parts_of_fullname) > 1:
            module_name = '.'.join(parts_of_fullname[0:-1])
            attribute_name = parts_of_fullname[-1]
            return {'module_name': module_name, 'attribute_name': attribute_name}

    @staticmethod
    def get_attr_of_module(module_name: str, attribute_name: str) -> object:
        """
            getattr(object, name[, default]) -> value

        Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
        When a default argument is given, it is returned when the attribute doesn't
        exist; without it, an exception is raised in that case.

        :param module_name: Fullname of module.
        :param attribute_name: Attribute name.
        :return: [Object] Attribute of module.
        """
        module = importlib.import_module(module_name)
        attribute = getattr(module, attribute_name)
        return attribute

    @staticmethod
    def attribute_exist(_object_name: object, attribute_name: str) -> object:
        """
            Return whether the object has an attribute with the given name.

            This is done by calling getattr(obj, name) and catching AttributeError.

        :param _object_name: Object name
        :param attribute_name: Attribute name
        """
        return hasattr(_object_name, attribute_name)
