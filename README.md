# generate-sdk-action

This action utilizes the [openapi-generator-cli](https://github.com/OpenAPITools/openapi-generator-cli) tool to build a client SDK based on certain action inputs. 

## Inputs

```yml
  branch-name: 
    description: Branch name
    required: true
  user-email: 
    description: Git user email
    default: dx@bandwidth.com
    required: false
  username: 
    description: Github auth username
    required: true
  token: 
    description: Github auth token
    required: true
  specs-organization: 
    description: Owner of the remote repository
    default: Bandwidth
    required: false
  specs-repository: 
    description: the remote repository to clone
    default: api-specs 
    required: false
  openapi-generator-version: 
    description: The OpenAPI Generator project version, in `6.0.1` format
    required: false
    default: '6.0.1'
  api-spec-path: 
    description: The destination of the API Specification to generate a client from
    required: false
    default: ./remote/bandwidth.json
  language: 
    description: The generator name (language) (`-g`) argument for the openapi-generator-cli
    required: true
  config:
    description: The configuration (`-c`) argument for the openapi-generator-cli
    required: true
```
