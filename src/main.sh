#!/bin/bash
echo '{"jsonrpc":"2.0","result":{"status":"success"},"id":1}'
while IFS= read -r line; do
    echo '{"jsonrpc":"2.0","result":{"status":"success"},"id":1}'
done