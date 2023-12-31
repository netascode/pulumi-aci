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
    'ChildArgs',
]

@pulumi.input_type
class ChildArgs:
    def __init__(__self__, *,
                 class_name: pulumi.Input[str],
                 rn: pulumi.Input[str],
                 content: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] class_name: Which class object is being created. (Make sure there is no colon in the classname)
        :param pulumi.Input[str] rn: Relative name of child object.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] content: Map of key-value pairs those needed to be passed to the Model object as parameters. Make sure the key name matches the name with the object parameter in ACI.
        """
        pulumi.set(__self__, "class_name", class_name)
        pulumi.set(__self__, "rn", rn)
        if content is not None:
            pulumi.set(__self__, "content", content)

    @property
    @pulumi.getter
    def class_name(self) -> pulumi.Input[str]:
        """
        Which class object is being created. (Make sure there is no colon in the classname)
        """
        return pulumi.get(self, "class_name")

    @class_name.setter
    def class_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "class_name", value)

    @property
    @pulumi.getter
    def rn(self) -> pulumi.Input[str]:
        """
        Relative name of child object.
        """
        return pulumi.get(self, "rn")

    @rn.setter
    def rn(self, value: pulumi.Input[str]):
        pulumi.set(self, "rn", value)

    @property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of key-value pairs those needed to be passed to the Model object as parameters. Make sure the key name matches the name with the object parameter in ACI.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "content", value)


