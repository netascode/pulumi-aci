// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { RestArgs } from "./rest";
export type Rest = import("./rest").Rest;
export const Rest: typeof import("./rest").Rest = null as any;
utilities.lazyLoad(exports, ["Rest"], () => require("./rest"));


const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aci:apic:Rest":
                return new Rest(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aci", "apic", _module)
