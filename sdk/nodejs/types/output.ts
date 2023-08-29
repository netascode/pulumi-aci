// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export namespace apic {
    export interface Child {
        /**
         * Which class object is being created. (Make sure there is no colon in the classname)
         */
        class_name: string;
        /**
         * Map of key-value pairs those needed to be passed to the Model object as parameters. Make sure the key name matches the name with the object parameter in ACI.
         */
        content?: {[key: string]: string};
        /**
         * Relative name of child object.
         */
        rn: string;
    }

}
