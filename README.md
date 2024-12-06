## Motivation

The Kaia ecosystem includes several websites tailored to specific purposes. For instance:

To swap FNSA assets to Kaia, visit the [portal](https://portal.kaia.io/).
For GC-related information, [Square](https://square.kaia.io/Home) is the go-to resource.
However, newcomers to the Kaia ecosystem may find it challenging to identify the right platform for their needs.

This PoC, Kaia Chatbot, demonstrates an intelligent assistant that guides users by identifying their intents and directing them to the appropriate Kaia website.

## How to start
1. Train a model with predefined data
```
> rasa train
```

2. Run a chatbot server
```
> rasa run
```

3. Request a message
```
curl -X POST \
http://localhost:5005/webhooks/rest/webhook \
-H "Content-Type: application/json" \
-d '{
  "message": "where can I access ongoing governance agenda of voting"
}'
```
