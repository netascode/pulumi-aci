# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'Child',
]

@pulumi.output_type
class Child(dict):
    def __init__(__self__, *,
                 class_name: str,
                 rn: str,
                 content: Optional[Mapping[str, str]] = None):
        """
        :param str class_name: Which class object is being created. (Make sure there is no colon in the classname)
        :param str rn: Relative name of child object.
        :param Mapping[str, str] content: Map of key-value pairs those needed to be passed to the Model object as parameters. Make sure the key name matches the name with the object parameter in ACI.
        """
        pulumi.set(__self__, "class_name", class_name)
        pulumi.set(__self__, "rn", rn)
        if content is not None:
            pulumi.set(__self__, "content", content)

    @property
    @pulumi.getter
    def class_name(self) -> str:
        """
        Which class object is being created. (Make sure there is no colon in the classname)
        """
        return pulumi.get(self, "class_name")

    @property
    @pulumi.getter
    def rn(self) -> str:
        """
        Relative name of child object.
        """
        return pulumi.get(self, "rn")

    @property
    @pulumi.getter
    def content(self) -> Optional[Mapping[str, str]]:
        """
        Map of key-value pairs those needed to be passed to the Model object as parameters. Make sure the key name matches the name with the object parameter in ACI.
        """
        return pulumi.get(self, "content")


