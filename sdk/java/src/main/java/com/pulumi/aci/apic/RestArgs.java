// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.aci.apic;

import com.pulumi.aci.apic.inputs.ChildArgs;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class RestArgs extends com.pulumi.resources.ResourceArgs {

    public static final RestArgs Empty = new RestArgs();

    /**
     * List of child objects to be created. Each child object must have a unique relative name.
     * 
     */
    @Import(name="children")
    private @Nullable Output<List<ChildArgs>> children;

    /**
     * @return List of child objects to be created. Each child object must have a unique relative name.
     * 
     */
    public Optional<Output<List<ChildArgs>>> children() {
        return Optional.ofNullable(this.children);
    }

    /**
     * Which class object is being created. (Make sure there is no colon in the classname)
     * 
     */
    @Import(name="class_name", required=true)
    private Output<String> class_name;

    /**
     * @return Which class object is being created. (Make sure there is no colon in the classname)
     * 
     */
    public Output<String> class_name() {
        return this.class_name;
    }

    /**
     * Map of key-value pairs those needed to be passed to the Model object as parameters. Make sure the key name matches the name with the object parameter in ACI.
     * 
     */
    @Import(name="content")
    private @Nullable Output<Map<String,String>> content;

    /**
     * @return Map of key-value pairs those needed to be passed to the Model object as parameters. Make sure the key name matches the name with the object parameter in ACI.
     * 
     */
    public Optional<Output<Map<String,String>>> content() {
        return Optional.ofNullable(this.content);
    }

    /**
     * Distinguished name of object being managed including its relative name, e.g. uni/tn-EXAMPLE_TENANT.
     * 
     */
    @Import(name="dn", required=true)
    private Output<String> dn;

    /**
     * @return Distinguished name of object being managed including its relative name, e.g. uni/tn-EXAMPLE_TENANT.
     * 
     */
    public Output<String> dn() {
        return this.dn;
    }

    private RestArgs() {}

    private RestArgs(RestArgs $) {
        this.children = $.children;
        this.class_name = $.class_name;
        this.content = $.content;
        this.dn = $.dn;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(RestArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private RestArgs $;

        public Builder() {
            $ = new RestArgs();
        }

        public Builder(RestArgs defaults) {
            $ = new RestArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param children List of child objects to be created. Each child object must have a unique relative name.
         * 
         * @return builder
         * 
         */
        public Builder children(@Nullable Output<List<ChildArgs>> children) {
            $.children = children;
            return this;
        }

        /**
         * @param children List of child objects to be created. Each child object must have a unique relative name.
         * 
         * @return builder
         * 
         */
        public Builder children(List<ChildArgs> children) {
            return children(Output.of(children));
        }

        /**
         * @param children List of child objects to be created. Each child object must have a unique relative name.
         * 
         * @return builder
         * 
         */
        public Builder children(ChildArgs... children) {
            return children(List.of(children));
        }

        /**
         * @param class_name Which class object is being created. (Make sure there is no colon in the classname)
         * 
         * @return builder
         * 
         */
        public Builder class_name(Output<String> class_name) {
            $.class_name = class_name;
            return this;
        }

        /**
         * @param class_name Which class object is being created. (Make sure there is no colon in the classname)
         * 
         * @return builder
         * 
         */
        public Builder class_name(String class_name) {
            return class_name(Output.of(class_name));
        }

        /**
         * @param content Map of key-value pairs those needed to be passed to the Model object as parameters. Make sure the key name matches the name with the object parameter in ACI.
         * 
         * @return builder
         * 
         */
        public Builder content(@Nullable Output<Map<String,String>> content) {
            $.content = content;
            return this;
        }

        /**
         * @param content Map of key-value pairs those needed to be passed to the Model object as parameters. Make sure the key name matches the name with the object parameter in ACI.
         * 
         * @return builder
         * 
         */
        public Builder content(Map<String,String> content) {
            return content(Output.of(content));
        }

        /**
         * @param dn Distinguished name of object being managed including its relative name, e.g. uni/tn-EXAMPLE_TENANT.
         * 
         * @return builder
         * 
         */
        public Builder dn(Output<String> dn) {
            $.dn = dn;
            return this;
        }

        /**
         * @param dn Distinguished name of object being managed including its relative name, e.g. uni/tn-EXAMPLE_TENANT.
         * 
         * @return builder
         * 
         */
        public Builder dn(String dn) {
            return dn(Output.of(dn));
        }

        public RestArgs build() {
            $.class_name = Objects.requireNonNull($.class_name, "expected parameter 'class_name' to be non-null");
            $.dn = Objects.requireNonNull($.dn, "expected parameter 'dn' to be non-null");
            return $;
        }
    }

}