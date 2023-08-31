# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 password: pulumi.Input[str],
                 url: pulumi.Input[str],
                 username: pulumi.Input[str],
                 insecure: Optional[pulumi.Input[bool]] = None,
                 logging: Optional[pulumi.Input[bool]] = None,
                 retries: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] password: Password for the APIC Account. This can also be set as the ACI_PASSWORD environment variable.
        :param pulumi.Input[str] url: URL of the Cisco APIC web interface. This can also be set as the ACI_URL environment variable.
        :param pulumi.Input[str] username: Username for the APIC Account. This can also be set as the ACI_USERNAME environment variable.
        :param pulumi.Input[bool] insecure: Allow insecure HTTPS client. This can also be set as the ACI_INSECURE environment variable. Defaults to true.
        :param pulumi.Input[bool] logging: Enable debug logging. This can also be set as the ACI_LOGGING environment variable. Defaults to false.
        :param pulumi.Input[int] retries: Number of retries for REST API calls. This can also be set as the ACI_RETRIES environment variable. Defaults to 3.
        """
        if password is None:
            password = (_utilities.get_env('ACI_PASSWORD') or '')
        pulumi.set(__self__, "password", password)
        if url is None:
            url = (_utilities.get_env('ACI_URL') or '')
        pulumi.set(__self__, "url", url)
        if username is None:
            username = (_utilities.get_env('ACI_USERNAME') or '')
        pulumi.set(__self__, "username", username)
        if insecure is not None:
            pulumi.set(__self__, "insecure", insecure)
        if logging is not None:
            pulumi.set(__self__, "logging", logging)
        if retries is not None:
            pulumi.set(__self__, "retries", retries)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        Password for the APIC Account. This can also be set as the ACI_PASSWORD environment variable.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        URL of the Cisco APIC web interface. This can also be set as the ACI_URL environment variable.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        """
        Username for the APIC Account. This can also be set as the ACI_USERNAME environment variable.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)

    @property
    @pulumi.getter
    def insecure(self) -> Optional[pulumi.Input[bool]]:
        """
        Allow insecure HTTPS client. This can also be set as the ACI_INSECURE environment variable. Defaults to true.
        """
        return pulumi.get(self, "insecure")

    @insecure.setter
    def insecure(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "insecure", value)

    @property
    @pulumi.getter
    def logging(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable debug logging. This can also be set as the ACI_LOGGING environment variable. Defaults to false.
        """
        return pulumi.get(self, "logging")

    @logging.setter
    def logging(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "logging", value)

    @property
    @pulumi.getter
    def retries(self) -> Optional[pulumi.Input[int]]:
        """
        Number of retries for REST API calls. This can also be set as the ACI_RETRIES environment variable. Defaults to 3.
        """
        return pulumi.get(self, "retries")

    @retries.setter
    def retries(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retries", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 insecure: Optional[pulumi.Input[bool]] = None,
                 logging: Optional[pulumi.Input[bool]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 retries: Optional[pulumi.Input[int]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Aci resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] insecure: Allow insecure HTTPS client. This can also be set as the ACI_INSECURE environment variable. Defaults to true.
        :param pulumi.Input[bool] logging: Enable debug logging. This can also be set as the ACI_LOGGING environment variable. Defaults to false.
        :param pulumi.Input[str] password: Password for the APIC Account. This can also be set as the ACI_PASSWORD environment variable.
        :param pulumi.Input[int] retries: Number of retries for REST API calls. This can also be set as the ACI_RETRIES environment variable. Defaults to 3.
        :param pulumi.Input[str] url: URL of the Cisco APIC web interface. This can also be set as the ACI_URL environment variable.
        :param pulumi.Input[str] username: Username for the APIC Account. This can also be set as the ACI_USERNAME environment variable.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Aci resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 insecure: Optional[pulumi.Input[bool]] = None,
                 logging: Optional[pulumi.Input[bool]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 retries: Optional[pulumi.Input[int]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            __props__.__dict__["insecure"] = pulumi.Output.from_input(insecure).apply(pulumi.runtime.to_json) if insecure is not None else None
            __props__.__dict__["logging"] = pulumi.Output.from_input(logging).apply(pulumi.runtime.to_json) if logging is not None else None
            if password is None:
                password = (_utilities.get_env('ACI_PASSWORD') or '')
            if password is None and not opts.urn:
                raise TypeError("Missing required property 'password'")
            __props__.__dict__["password"] = None if password is None else pulumi.Output.secret(password)
            __props__.__dict__["retries"] = pulumi.Output.from_input(retries).apply(pulumi.runtime.to_json) if retries is not None else None
            if url is None:
                url = (_utilities.get_env('ACI_URL') or '')
            if url is None and not opts.urn:
                raise TypeError("Missing required property 'url'")
            __props__.__dict__["url"] = url
            if username is None:
                username = (_utilities.get_env('ACI_USERNAME') or '')
            if username is None and not opts.urn:
                raise TypeError("Missing required property 'username'")
            __props__.__dict__["username"] = username
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["password"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Provider, __self__).__init__(
            'aci',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[str]:
        """
        Password for the APIC Account. This can also be set as the ACI_PASSWORD environment variable.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        URL of the Cisco APIC web interface. This can also be set as the ACI_URL environment variable.
        """
        return pulumi.get(self, "url")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[str]:
        """
        Username for the APIC Account. This can also be set as the ACI_USERNAME environment variable.
        """
        return pulumi.get(self, "username")

