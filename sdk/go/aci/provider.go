// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package aci

import (
	"context"
	"reflect"

	"errors"
	"github.com/netascode/pulumi-aci/sdk/go/aci/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type Provider struct {
	pulumi.ProviderResourceState

	// Password for the APIC Account. This can also be set as the ACI_PASSWORD environment variable.
	Password          pulumi.StringOutput    `pulumi:"password"`
	PluginDownloadURL pulumi.StringPtrOutput `pulumi:"pluginDownloadURL"`
	// URL of the Cisco APIC web interface. This can also be set as the ACI_URL environment variable.
	Url pulumi.StringOutput `pulumi:"url"`
	// Username for the APIC Account. This can also be set as the ACI_USERNAME environment variable.
	Username pulumi.StringOutput    `pulumi:"username"`
	Version  pulumi.StringPtrOutput `pulumi:"version"`
}

// NewProvider registers a new resource with the given unique name, arguments, and options.
func NewProvider(ctx *pulumi.Context,
	name string, args *ProviderArgs, opts ...pulumi.ResourceOption) (*Provider, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Password == nil {
		if d := internal.GetEnvOrDefault("", nil, "ACI_PASSWORD"); d != nil {
			args.Password = pulumi.String(d.(string))
		}
	}
	if args.Url == nil {
		if d := internal.GetEnvOrDefault("", nil, "ACI_URL"); d != nil {
			args.Url = pulumi.String(d.(string))
		}
	}
	if args.Username == nil {
		if d := internal.GetEnvOrDefault("", nil, "ACI_USERNAME"); d != nil {
			args.Username = pulumi.String(d.(string))
		}
	}
	if args.Password != nil {
		args.Password = pulumi.ToSecret(args.Password).(pulumi.StringInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"password",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Provider
	err := ctx.RegisterResource("pulumi:providers:aci", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type providerArgs struct {
	// Allow insecure HTTPS client. This can also be set as the ACI_INSECURE environment variable. Defaults to true.
	Insecure *bool `pulumi:"insecure"`
	// Enable debug logging. This can also be set as the ACI_LOGGING environment variable. Defaults to false.
	Logging *bool `pulumi:"logging"`
	// Password for the APIC Account. This can also be set as the ACI_PASSWORD environment variable.
	Password          string  `pulumi:"password"`
	PluginDownloadURL *string `pulumi:"pluginDownloadURL"`
	// Number of retries for REST API calls. This can also be set as the ACI_RETRIES environment variable. Defaults to 3.
	Retries *int `pulumi:"retries"`
	// URL of the Cisco APIC web interface. This can also be set as the ACI_URL environment variable.
	Url string `pulumi:"url"`
	// Username for the APIC Account. This can also be set as the ACI_USERNAME environment variable.
	Username string  `pulumi:"username"`
	Version  *string `pulumi:"version"`
}

// The set of arguments for constructing a Provider resource.
type ProviderArgs struct {
	// Allow insecure HTTPS client. This can also be set as the ACI_INSECURE environment variable. Defaults to true.
	Insecure pulumi.BoolPtrInput
	// Enable debug logging. This can also be set as the ACI_LOGGING environment variable. Defaults to false.
	Logging pulumi.BoolPtrInput
	// Password for the APIC Account. This can also be set as the ACI_PASSWORD environment variable.
	Password          pulumi.StringInput
	PluginDownloadURL pulumi.StringPtrInput
	// Number of retries for REST API calls. This can also be set as the ACI_RETRIES environment variable. Defaults to 3.
	Retries pulumi.IntPtrInput
	// URL of the Cisco APIC web interface. This can also be set as the ACI_URL environment variable.
	Url pulumi.StringInput
	// Username for the APIC Account. This can also be set as the ACI_USERNAME environment variable.
	Username pulumi.StringInput
	Version  pulumi.StringPtrInput
}

func (ProviderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*providerArgs)(nil)).Elem()
}

type ProviderInput interface {
	pulumi.Input

	ToProviderOutput() ProviderOutput
	ToProviderOutputWithContext(ctx context.Context) ProviderOutput
}

func (*Provider) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (i *Provider) ToProviderOutput() ProviderOutput {
	return i.ToProviderOutputWithContext(context.Background())
}

func (i *Provider) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProviderOutput)
}

type ProviderOutput struct{ *pulumi.OutputState }

func (ProviderOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (o ProviderOutput) ToProviderOutput() ProviderOutput {
	return o
}

func (o ProviderOutput) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return o
}

// Password for the APIC Account. This can also be set as the ACI_PASSWORD environment variable.
func (o ProviderOutput) Password() pulumi.StringOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringOutput { return v.Password }).(pulumi.StringOutput)
}

func (o ProviderOutput) PluginDownloadURL() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.PluginDownloadURL }).(pulumi.StringPtrOutput)
}

// URL of the Cisco APIC web interface. This can also be set as the ACI_URL environment variable.
func (o ProviderOutput) Url() pulumi.StringOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringOutput { return v.Url }).(pulumi.StringOutput)
}

// Username for the APIC Account. This can also be set as the ACI_USERNAME environment variable.
func (o ProviderOutput) Username() pulumi.StringOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringOutput { return v.Username }).(pulumi.StringOutput)
}

func (o ProviderOutput) Version() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Version }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ProviderInput)(nil)).Elem(), &Provider{})
	pulumi.RegisterOutputType(ProviderOutput{})
}
