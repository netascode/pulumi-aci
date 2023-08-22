// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class Provider extends pulumi.ProviderResource {
    /** @internal */
    public static readonly __pulumiType = 'aci';

    /**
     * Returns true if the given object is an instance of Provider.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Provider {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === "pulumi:providers:" + Provider.__pulumiType;
    }

    /**
     * Password for the APIC Account. This can also be set as the ACI_PASSWORD environment variable.
     */
    public readonly password!: pulumi.Output<string>;
    /**
     * URL of the Cisco APIC web interface. This can also be set as the ACI_URL environment variable.
     */
    public readonly url!: pulumi.Output<string>;
    /**
     * Username for the APIC Account. This can also be set as the ACI_USERNAME environment variable.
     */
    public readonly username!: pulumi.Output<string>;
    public readonly version!: pulumi.Output<string | undefined>;

    /**
     * Create a Provider resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ProviderArgs, opts?: pulumi.ResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        {
            if ((!args || args.password === undefined) && !opts.urn) {
                throw new Error("Missing required property 'password'");
            }
            if ((!args || args.url === undefined) && !opts.urn) {
                throw new Error("Missing required property 'url'");
            }
            if ((!args || args.username === undefined) && !opts.urn) {
                throw new Error("Missing required property 'username'");
            }
            resourceInputs["insecure"] = pulumi.output(args ? args.insecure : undefined).apply(JSON.stringify);
            resourceInputs["logging"] = pulumi.output(args ? args.logging : undefined).apply(JSON.stringify);
            resourceInputs["password"] = (args?.password ? pulumi.secret(args.password) : undefined) ?? (utilities.getEnv("ACI_PASSWORD") || "");
            resourceInputs["retries"] = pulumi.output(args ? args.retries : undefined).apply(JSON.stringify);
            resourceInputs["url"] = (args ? args.url : undefined) ?? (utilities.getEnv("ACI_URL") || "");
            resourceInputs["username"] = (args ? args.username : undefined) ?? (utilities.getEnv("ACI_USERNAME") || "");
            resourceInputs["version"] = args ? args.version : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["password"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(Provider.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Provider resource.
 */
export interface ProviderArgs {
    /**
     * Allow insecure HTTPS client. This can also be set as the ACI_INSECURE environment variable. Defaults to true.
     */
    insecure?: pulumi.Input<boolean>;
    /**
     * Enable debug logging. This can also be set as the ACI_LOGGING environment variable. Defaults to false.
     */
    logging?: pulumi.Input<boolean>;
    /**
     * Password for the APIC Account. This can also be set as the ACI_PASSWORD environment variable.
     */
    password: pulumi.Input<string>;
    /**
     * Number of retries for REST API calls. This can also be set as the ACI_RETRIES environment variable. Defaults to 3.
     */
    retries?: pulumi.Input<number>;
    /**
     * URL of the Cisco APIC web interface. This can also be set as the ACI_URL environment variable.
     */
    url: pulumi.Input<string>;
    /**
     * Username for the APIC Account. This can also be set as the ACI_USERNAME environment variable.
     */
    username: pulumi.Input<string>;
    version?: pulumi.Input<string>;
}
