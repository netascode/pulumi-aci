// Copyright © 2023 Cisco Systems, Inc. and its affiliates.
// All rights reserved.
//
// Licensed under the Mozilla Public License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     https://mozilla.org/MPL/2.0/
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
// SPDX-License-Identifier: MPL-2.0

package provider

import (
	"strings"

	"github.com/blang/semver"
	p "github.com/pulumi/pulumi-go-provider"
	"github.com/pulumi/pulumi-go-provider/infer"
	"github.com/pulumi/pulumi-go-provider/middleware/schema"

	apic "github.com/netascode/pulumi-aci/provider/pkg/provider/apic"
	"github.com/pulumi/pulumi-go-provider/integration"
)

// This provider uses the `pulumi-go-provider` library to produce a code-first provider definition.
func NewProvider() p.Provider {
	return infer.Provider(infer.Options{
		// This is the metadata for the provider
		Metadata: schema.Metadata{
			DisplayName: "Aci",
			Description: "The Pulumi ACI provider provides resources to interact with a Cisco ACI fabric.",
			Keywords: []string{
				"pulumi",
				"aci",
				"networking",
				"cisco",
			},
			Homepage:   "https://pulumi.com",
			License:    "Apache-2.0",
			Repository: "https://github.com/netascode/pulumi-aci",
			Publisher:  "Cisco",
			LogoURL:    "https://raw.githubusercontent.com/netascode/pulumi-aci/master/assets/logo.png",
			// This contains language specific details for generating the provider's SDKs
			LanguageMap: map[string]any{
				"csharp": map[string]any{
					"packageReferences": map[string]string{
						"Pulumi": "3.*",
					},
				},
				"go": map[string]any{
					"generateResourceContainerTypes": true,
					"importBasePath":                 "github.com/netascode/pulumi-aci/sdk/go/aci",
				},
				"nodejs": map[string]any{
					"packageName": "@netascode/aci",
					"dependencies": map[string]string{
						"@pulumi/pulumi": "^3.0.0",
					},
				},
				"python": map[string]any{
					"requires": map[string]string{
						"pulumi": ">=3.0.0,<4.0.0",
					},
				},
				"java": map[string]any{
					"buildFiles":                      "gradle",
					"gradleNexusPublishPluginVersion": "1.1.0",
					"dependencies": map[string]any{
						"com.pulumi:pulumi":               "0.6.0",
						"com.google.code.gson:gson":       "2.8.9",
						"com.google.code.findbugs:jsr305": "3.0.2",
					},
				},
			},
		},
		// A list of `infer.Resource` that are provided by the provider.
		Resources: []infer.InferredResource{
			infer.Resource[*apic.Rest, apic.RestInputs, apic.RestOutputs](),
		},
		Config: infer.Config[*apic.Config](),
	})
}

func Schema(version string) (string, error) {
	version = strings.TrimPrefix(version, "v")
	s, err := integration.NewServer("aci", semver.MustParse(version), NewProvider()).
		GetSchema(p.GetSchemaRequest{})
	return s.Schema, err
}
