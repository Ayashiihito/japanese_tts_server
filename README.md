# jtts server

is a wrapper around [espnet](https://github.com/espnet/espnet), an end-to-end speech processing toolkit, which is used to generate speech from text

## API

POST `/audio`
```json
{
  "text": "こんにちは"
}
```

returns a `.wav` file for this text

# Requirements:
A GPU that supports CUDA

## Supported platforms:
Linux, Windows (via WSL), MacOS (haven't tried that)

### TODO
- [ ] Make address and port configurable
- [ ] Add an option to use CPU when GPU is not available 
- [ ] Configure to run inside Docker
- [ ] Run server in production mode
