# generate-sdk-action

This action utilizes the [openapi-generator-cli](https://github.com/OpenAPITools/openapi-generator-cli) tool to build a client SDK based on certain action inputs. 

## Inputs

```yml
branch-name: 
  description: Branch name
  required: true
token: 
  description: Github auth token
  required: true
language: 
  description: The generator name (language) (`-g`) argument for the openapi-generator-cli
  required: true
config:
  description: The configuration (`-c`) argument for the openapi-generator-cli
  required: true
user-email: 
  description: Git user email
  default: dx@bandwidth.com
  required: false
username: 
  description: Github username
  default: DX-Bandwidth
  required: false
openapi-generator-version: 
  description: The OpenAPI Generator project version, in `x.x.x` format
  required: false
  default: '6.5.0'
api-spec-path: 
  description: The destination of the API Specification to generate a client from
  required: false
  default: ./bandwidth.yml
```

## Outputs

```yml
changes: 
  description: Boolean representing if files in the SDK were changed or not.
```
