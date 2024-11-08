# generate-sdk-action

This action utilizes the [openapi-generator-cli](https://github.com/OpenAPITools/openapi-generator-cli) tool to build a client SDK based on certain action inputs. 

## Inputs

```yml
language: 
  description: The generator name (language) (`-g`) argument for the openapi-generator-cli
  required: true
config:
  description: The configuration (`-c`) argument for the openapi-generator-cli
  required: false
  default: ./openapi-config.yml
api-spec-path: 
  description: The destination of the API Specification to generate a client from
  required: false
  default: ./bandwidth.yml
openapi-generator-version: 
  description: The OpenAPI Generator project version, in `x.x.x` format
  required: false
  default: '7.6.0'
additional-properties:
  description: Additional properties to pass to the generator
  required: false
  default: ''
working-directory: 
  description: The working directory to run the action in
  required: false
  default: ./
```
