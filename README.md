# jtts server

is a wrapper around [espnet](https://github.com/espnet/espnet), an end-to-end speech processing toolkit, which is used to generate speech from text.  
It can be used on it's own as well as with [jtts client](https://github.com/Ayashiihito/japanese_tts_client_rs)

## API
POST `/audio`
```json
{
  "text": "こんにちは"
}
```

returns a `.wav` file for this text

## Requirements:
- A GPU that supports CUDA

## Supported platforms:
- Linux
- Windows (only via WSL)
- MacOS (haven't tried that)

## TODO:
- [ ] Make address and port configurable
- [ ] Add an option to use CPU when GPU is not available 
- [ ] Configure to run inside Docker
- [ ] Run server in production mode
- [ ] Support languages other than Japanese
