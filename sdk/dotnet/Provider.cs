// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aci
{
    [AciResourceType("pulumi:providers:aci")]
    public partial class Provider : global::Pulumi.ProviderResource
    {
        /// <summary>
        /// Password for the APIC Account. This can also be set as the ACI_PASSWORD environment variable.
        /// </summary>
        [Output("password")]
        public Output<string> Password { get; private set; } = null!;

        /// <summary>
        /// URL of the Cisco APIC web interface. This can also be set as the ACI_URL environment variable.
        /// </summary>
        [Output("url")]
        public Output<string> Url { get; private set; } = null!;

        /// <summary>
        /// Username for the APIC Account. This can also be set as the ACI_USERNAME environment variable.
        /// </summary>
        [Output("username")]
        public Output<string> Username { get; private set; } = null!;

        [Output("version")]
        public Output<string?> Version { get; private set; } = null!;


        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs args, CustomResourceOptions? options = null)
            : base("aci", name, args ?? new ProviderArgs(), MakeResourceOptions(options, ""))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                AdditionalSecretOutputs =
                {
                    "password",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class ProviderArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Allow insecure HTTPS client. This can also be set as the ACI_INSECURE environment variable. Defaults to true.
        /// </summary>
        [Input("insecure", json: true)]
        public Input<bool>? Insecure { get; set; }

        /// <summary>
        /// Enable debug logging. This can also be set as the ACI_LOGGING environment variable. Defaults to false.
        /// </summary>
        [Input("logging", json: true)]
        public Input<bool>? Logging { get; set; }

        [Input("password", required: true)]
        private Input<string>? _password;

        /// <summary>
        /// Password for the APIC Account. This can also be set as the ACI_PASSWORD environment variable.
        /// </summary>
        public Input<string>? Password
        {
            get => _password;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _password = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// Number of retries for REST API calls. This can also be set as the ACI_RETRIES environment variable. Defaults to 3.
        /// </summary>
        [Input("retries", json: true)]
        public Input<int>? Retries { get; set; }

        /// <summary>
        /// URL of the Cisco APIC web interface. This can also be set as the ACI_URL environment variable.
        /// </summary>
        [Input("url", required: true)]
        public Input<string> Url { get; set; } = null!;

        /// <summary>
        /// Username for the APIC Account. This can also be set as the ACI_USERNAME environment variable.
        /// </summary>
        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        [Input("version")]
        public Input<string>? Version { get; set; }

        public ProviderArgs()
        {
            Password = Utilities.GetEnv("ACI_PASSWORD") ?? "";
            Url = Utilities.GetEnv("ACI_URL") ?? "";
            Username = Utilities.GetEnv("ACI_USERNAME") ?? "";
        }
        public static new ProviderArgs Empty => new ProviderArgs();
    }
}
