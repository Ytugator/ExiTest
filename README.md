# ExiTest

```
verify
├── Correct methods and status codes (for "throw service")
├── Request payloads (for "throw service")
├── Functional
│   ├── Correct implementation 
│   │   ├── WebSocket
│   │   │   ├── Conncetion
│   │   │   │   ├── Positive check: should be established
│   │   │   │   └── Negative check: shouldnt be established if invalid protocol
│   │   │   └── Responce
│   │   │       └── correct status codes
│   │   │           ├── send an empty message
│   │   │           └── unsupported message type    
│   │   └── gRPC
│   │       ├── Conncetion
│   │       │   ├── Positive check: should be established
│   │       │   └── Negative check: shouldnt be established if invalid protocol
│   │       └── Responce
│   │           └── correct status codes
│   │               ├── send an empty message
│   │               └── unsupported message type
│   └── Business logic
│       ├── Should start sending response messages after a valid request message
│       ├── Response should be parsable and the values of the keys must be valid
│       └── server should not respond to an invalid request message.
├── Integrational 
└── Non-funtional
    ├── Response timing
    ├── Perfomance
    ├── Stress
    └── WS/WSS
```